from typing import Dict, List

from .contracts import OptimizationRequest, OptimizationResult


def _dot(x: List[float], y: List[float]) -> float:
    return sum(a * b for a, b in zip(x, y))


def _mat_vec(m: List[List[float]], v: List[float]) -> List[float]:
    return [_dot(row, v) for row in m]


def baseline_optimize(request: OptimizationRequest) -> OptimizationResult:
    k = request.order.horizon_buckets
    if k <= 0:
        raise ValueError("horizon_buckets must be positive")
    if request.risk_aversion < 0:
        raise ValueError("risk_aversion must be non-negative")

    schedule: Dict[str, List[float]] = {}
    for asset_order in request.order.orders:
        per_bucket = asset_order.quantity / k
        cap = request.market.max_participation.get(asset_order.asset_id)
        if cap is not None and abs(per_bucket) > cap:
            raise ValueError(f"participation cap violated for {asset_order.asset_id}")
        schedule[asset_order.asset_id] = [per_bucket for _ in range(k)]

    asset_index = {asset_id: idx for idx, asset_id in enumerate(request.market.asset_ids)}
    trade_vector = [0.0 for _ in request.market.asset_ids]
    for asset_order in request.order.orders:
        idx = asset_index.get(asset_order.asset_id)
        if idx is None:
            raise ValueError(f"asset_id not in market snapshot: {asset_order.asset_id}")
        trade_vector[idx] = asset_order.quantity / k

    impact_vec = _mat_vec(request.market.temporary_impact, trade_vector)
    expected_cost = _dot(trade_vector, impact_vec) * k

    cov_vec = _mat_vec(request.market.covariance, trade_vector)
    risk_proxy = request.risk_aversion * _dot(trade_vector, cov_vec) * k

    return OptimizationResult(
        schedule=schedule,
        expected_cost=expected_cost,
        risk_proxy=risk_proxy,
    )
