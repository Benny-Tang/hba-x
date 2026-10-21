# HBA-X — Independent Positioning Experiment

HBA-X is a separate research workspace for testing positioning and risk-control hypotheses against the corrected HBA reference implementation.

## Current status
This package provides initial portfolio primitives and unit tests only. It is **not** a reproduction of HBA and does not claim trading performance.

## Install and test
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Important
- Keep `hba-provenance` unchanged.
- Do not put broker credentials, API tokens, `.env` files, or private account data in this repository.
- Connect the corrected reference engine and its required data before claiming benchmark reproduction.

