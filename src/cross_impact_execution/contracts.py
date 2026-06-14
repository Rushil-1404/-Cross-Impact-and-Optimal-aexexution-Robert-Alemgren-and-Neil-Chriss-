from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class AssetOrder:
    asset_id: str
    quantity: float


@dataclass(frozen=True)
class BasketOrder:
    horizon_buckets: int
    bucket_seconds: int
    orders: List[AssetOrder]


@dataclass(frozen=True)
class MarketSnapshot:
    asset_ids: List[str]
    covariance: List[List[float]]
    temporary_impact: List[List[float]]
    max_participation: Dict[str, float]


@dataclass(frozen=True)
class OptimizationRequest:
    order: BasketOrder
    market: MarketSnapshot
    risk_aversion: float


@dataclass(frozen=True)
class OptimizationResult:
    schedule: Dict[str, List[float]]
    expected_cost: float
    risk_proxy: float
