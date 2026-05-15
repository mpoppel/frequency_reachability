# frequency_reachability

Code for the paper:
**"Grid-Based Initialization Resolves Frequency Reachability in Trainable-Frequency Quantum Machine Learning"**

## Repository structure

```
frequency_reachability/
├── paper_style.py                    # Shared matplotlib style — import in every notebook
├── requirements.txt
├── datasets/
│   ├── 00_generate_synthetic.ipynb   # Generate all synthetic target function datasets
│   ├── datasets_1d_jaderberg.pkl     # Ω₁ = {1, 1.2, 3}
│   ├── datasets_1d_jaderberg_10.pkl  # Ω₂ = {11, 11.2, 13}
│   └── datasets_1d_jaderberg_GaussianShift.pkl
└── experiments/
    ├── 01_synthetic_benchmark.ipynb  # Main Ω₁/Ω₂ results + frequency offset sweep
    ├── 02_gradient_analysis.ipynb    # Prefactor displacement + gradient sweep
    ├── 03_alternative_optimizers.ipynb  # CMA-ES + random uniform init
    ├── 04_real_world.ipynb           # Flight Passengers + California Housing
    └── 05_ablation.ipynb             # Encoding base + circuit architecture ablations
```

## Reproducing the paper results

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate datasets
Run `datasets/00_generate_synthetic.ipynb` once. The `.pkl` files are also
provided pre-generated in the `datasets/` directory.

### 3. Run experiments
Run notebooks `01` through `05` in order. Each notebook:
- Saves results as CSV files in an `experiments/results/` subdirectory
- Generates the corresponding paper figures as PDF + PNG

### Smoke test
Set `SMOKE_TEST = True` at the top of any experiment notebook to run a fast
end-to-end check (1 function, 2 seeds, 50–100 steps) before committing to
a full run.

## Figures → notebooks

| Paper figure | Notebook |
|---|---|
| Fig. 1 (function fitting) | `01_synthetic_benchmark.ipynb` |
| Fig. 2 (displacement + gradient sweep) | `02_gradient_analysis.ipynb` |
| Fig. 3 (R² frequency offset robustness) | `01_synthetic_benchmark.ipynb` |
| Fig. 4 (CMA-ES + baseline table) | `03_alternative_optimizers.ipynb` |
| Fig. 5 (real-world R² distributions) | `04_real_world.ipynb` |
| Fig. 6 (ablation) | `05_ablation.ipynb` |
| Appendix figures | `02_gradient_analysis.ipynb` |


```
