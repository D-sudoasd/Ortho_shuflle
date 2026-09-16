<p align="center">
  <img src="assets/readme/hero.svg" width="100%" alt="CrystalShift XRD: Cmcm 4c theoretical powder XRD workbench.">
</p>

# CrystalShift XRD

**How lattice, Wyckoff `y`, basal shuffle, and energy move powder peaks and F².**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-green.svg)](https://www.python.org/downloads/)
[![version](https://img.shields.io/badge/version-2.3.0-lightgrey.svg)](pyproject.toml)

Streamlit workbench for theoretical powder XRD of orthorhombic **`Cmcm 4c`**. Package version `2.3.0` · export schema `2.4`.

> Repository folder name `Ortho_shuflle` keeps the historical typo — do not rename the remote.

> Theoretical model only — not Rietveld, not absolute intensity calibration.

<p align="center">
  <img src="assets/readme/section-01-model.svg" width="100%" alt="01 Model: Cmcm 4c structure contract.">
</p>

## Model contract

```text
(0, y, 1/4), (0, -y, 3/4),
(1/2, 1/2+y, 1/4), (1/2, 1/2-y, 3/4)

shuffle_signed     = 2*(y-0.25)
shuffle_magnitude  = |shuffle_signed|
normalized_shuffle = shuffle_magnitude / 0.5   # in [0, 1]
wavelength_A   = 12.398419843320026 / energy_keV
I_model_peak   = F² × applied_multiplicity × applied_LP × applied_volume_factor × line_weight
applied_volume_factor = 1 / V_cell when the cell-volume correction is enabled; otherwise 1
```

`R_hkl` with/without LP is for experimental area post-processing (theoretical only).

## Install / Quick start

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m streamlit run app.py --server.port 8508
```

Open http://localhost:8508/  
Windows launcher: `启动 CrystalShift XRD.bat`

## Usage

<p align="center">
  <img src="assets/readme/section-02-explore.svg" width="100%" alt="02 Explore: live frames, sweeps, peak fit.">
</p>

- **Pattern** — static 2θ / *q* / *d*
- **Live evolution** — exact precomputed frames; browser switches locally
- **F² evolution** + structure preview along `b`
- **Sweep / trajectory** CSV · **discrete-peak fit** diagnostics
- Schema 2.4 ZIP + `analysis.xlsx` with hashes and checksums

## Scientific boundary — what it is NOT

Does **not** implement Rietveld / Le Bail / Pawley, texture, absorption, size/strain broadening, zero shift, background, phase fractions, or absolute intensity calibration.

## Tests

```bash
python -m pytest -q && python -m ruff check .
```

## License

MIT — see [`LICENSE`](LICENSE). Cite the structure source and keep export manifests with figures.
