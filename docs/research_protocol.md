# HBA-X Research Protocol

## Purpose
Independent positioning-engine research. The reference HBA repository remains unchanged.

## First milestone
Implement and test portfolio primitives. These are scaffolding only, not a reproduction of HBA.

## Validation requirements
- Preserve zero weights and close dropped positions.
- Use only information available at the decision timestamp.
- Match reference data, costs, universe, and walk-forward splits before comparing results.
- Keep the final holdout untouched during model selection.
- Record failed experiments as well as successful ones.
- Do not claim benchmark reproduction until the reference evaluation has been run.

## Initial experiment sequence
1. Reproduce the corrected HBA benchmark.
2. Test a predeclared adaptive-exposure hypothesis.
3. Test drawdown controls separately from the positioning model.
4. Compare all candidates with identical evaluation rules and costs.

