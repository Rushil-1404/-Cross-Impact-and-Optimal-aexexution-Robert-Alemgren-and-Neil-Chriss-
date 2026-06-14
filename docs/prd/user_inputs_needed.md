# Inputs Needed from You

## Trading / Product Inputs
1. Asset universe scope (single region, multi-region, asset classes).
2. Typical basket size and max expected basket size.
3. Standard execution horizons (e.g., 15m, 1h, 1d).
4. Hard participation constraints by asset or globally.

## Quant Inputs
1. Preferred calibration horizon for covariance and impact matrices.
2. Initial temporary cross-impact estimation method.
3. Whether permanent impact is in MVP scope.
4. Default lambda range for scenario analysis.

## Engineering Inputs
1. Preferred runtime stack for API (FastAPI/Flask/other).
2. Deployment target (local only, container, cloud).
3. Required observability stack (logs/metrics/tracing).

## Validation Inputs
1. Baseline benchmark to compare against (TWAP/VWAP/single-asset AC).
2. Success metric thresholds (expected shortfall reduction target).
3. Historical dataset source and format for backtests.
