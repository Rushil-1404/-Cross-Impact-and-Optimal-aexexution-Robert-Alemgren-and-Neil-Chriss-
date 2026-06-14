# Technical PRD: Cross-Impact & Optimal Execution

## 1. Document Control
- Version: 0.1.0
- Status: Draft (implementation starter)
- Authors: TBD
- Reviewers: Trading, Quant Research, Engineering, Risk
- Created: 2026-06-14
- Last Updated: 2026-06-14

## 2. Executive Summary
Build a multi-asset execution optimizer extending Almgren-Chriss to model cross-impact and generate feasible execution schedules under operational constraints.

## 3. Problem Statement
Current single-asset execution logic ignores cross-impact effects between correlated instruments, increasing slippage and inventory risk for baskets and portfolio rebalancing.

## 4. Goals
1. Produce feasible multi-asset schedules for a given horizon.
2. Include temporary cross-impact in expected execution cost.
3. Expose transparent cost-risk tradeoff control.
4. Enforce hard constraints: participation, horizon, inventory direction.

## 5. Non-Goals (MVP)
1. Venue-level smart order routing.
2. Tick-level execution adaptation.
3. Reinforcement-learning policy replacement.

## 6. Users & Stakeholders
- Primary: Execution trader
- Secondary: Quant researcher, risk, compliance, engineering

## 7. Functional Requirements
### FR-1 Order Intake
- Input: Basket order with per-asset side/quantity and horizon.
- Output: Validated internal order object.

### FR-2 Market/Model Intake
- Input: Covariance matrix, temporary cross-impact matrix, liquidity constraints.
- Output: Validated model inputs for optimizer.

### FR-3 Optimization
- Input: Order + model inputs + risk aversion lambda.
- Output: Time-bucket schedule per asset, expected cost, risk proxy.

### FR-4 Constraint Validation
- Enforce non-negative participation, horizon buckets, and direction-consistent liquidation.

### FR-5 Scenario Runner
- Support multiple lambda values and return comparative summaries.

## 8. Non-Functional Requirements
- Runtime target: <= 2s for up to 50 assets and 20 buckets (single request)
- Deterministic outputs for identical inputs
- Full request-response audit logging (without secrets)
- Graceful failures with explicit validation errors

## 9. Quant Model Specification
Objective (MVP form):
- Minimize expected temporary-impact cost + lambda * inventory risk proxy.
- Include cross terms via temporary impact matrix G.

Discrete dynamics:
- x[k+1] = x[k] - v[k] * dt
- x[0] = initial inventory
- x[K] ~= 0

Core constraints:
- v[k] must satisfy participation caps
- liquidation direction must match order side

## 10. Data Contracts
Canonical input entities are defined in `src/cross_impact_execution/contracts.py`:
- AssetOrder
- BasketOrder
- MarketSnapshot
- OptimizationRequest
- OptimizationResult

## 11. System Design (MVP)
1. API layer validates request shape.
2. Contracts layer normalizes entities.
3. Optimizer service computes schedule.
4. Reporter returns schedule + summary metrics.

## 12. Testing Strategy
- Unit tests for validation and schedule construction.
- Property checks for inventory monotonicity and horizon completion.
- Regression tests with fixed synthetic matrices.

## 13. Risks
1. Unstable cross-impact estimates -> apply shrinkage/regularization.
2. Ill-conditioned covariance/impact matrices -> validation + fallback.
3. Overly strict constraints causing infeasibility -> surface diagnostics.

## 14. Milestones
1. M1: Contracts + baseline optimizer interface
2. M2: Matrix-aware objective implementation
3. M3: Scenario comparison + reporting
4. M4: Integration and pilot backtests

## 15. Open Inputs Required from User
See `docs/prd/user_inputs_needed.md`.
