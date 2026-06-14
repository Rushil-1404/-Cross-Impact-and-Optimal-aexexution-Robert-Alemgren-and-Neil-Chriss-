# Cross Impact and Optimal Execution (Almgren-Chriss Extension)

This repository contains a technical foundation for a multi-asset cross-impact execution framework inspired by Robert Almgren and Neil Chriss.

## Project Structure
- `docs/prd/technical_prd.md`: implementation-focused technical PRD
- `docs/prd/user_inputs_needed.md`: open inputs required from stakeholders
- `docs/specs/api_contract.yaml`: API contract for optimization service
- `configs/model.default.yaml`: default model and runtime configuration
- `src/cross_impact_execution/contracts.py`: canonical request/response data contracts
- `src/cross_impact_execution/optimizer.py`: baseline optimizer implementation

## Current Status
- Baseline contracts and optimizer scaffold are available.
- API and config templates are defined for implementation.
- Additional calibration and solver upgrades are pending user inputs.

## Next Steps
1. Confirm open inputs listed in `docs/prd/user_inputs_needed.md`.
2. Finalize model assumptions and calibration pipeline.
3. Implement full constrained optimizer and scenario runner.
