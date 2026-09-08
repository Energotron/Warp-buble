# Non-minimal gravity: standard sirens expose a concrete GW-friction signature and H0 bias

- **Accepted:** 2026-09-08 04:09 +03:00
- **Classification:** observation-facing model test / scalar-tensor modified gravity / non-minimal coupling / gravitational-wave propagation / standard sirens
- **Primary source:** arXiv:2609.04112v1, *Consistency between cosmological and standard siren observations in evolving dark energy* (submitted 2026-09-03)
- **Source quality:** primary technical preprint using the previously cosmology-favored non-minimally coupled scalar model, DESI-DR2 + Planck/ACT + DES-Dovekie posteriors, and public GWTC-5 modified-propagation posteriors; explicit mappings to `c_M` and `(Xi_0,n)` are given. Not yet peer reviewed.
- **Status:** accepted as significant and non-duplicate relative to the current modified-gravity index/checkpoint.

## Core result

The non-minimally coupled scalar-tensor model already favored over `ΛCDM` by the cited cosmological background data predicts a specific modified gravitational-wave propagation signal rather than merely a background-level deviation.

The paper finds:

1. The model predicts a low-redshift running of the effective Planck mass with `α_M(z=0) = -0.76^{+0.37}_{-0.42}`, decaying toward zero by `z ~ 2`.
2. This drives a gravitational-wave luminosity distance smaller than the electromagnetic one, with `D_L^GW / D_L^EM ≃ 0.88` by `z ~ 1.5`.
3. Projected onto common phenomenological templates, the model gives `c_M = -0.5 ± 0.2` and `(Xi_0,n) = (0.88 ± 0.05, 3.2 ± 0.3)`.
4. These predictions are still fully consistent with current GWTC-5 standard-siren propagation constraints, because present uncertainties are broad enough to include both the NMC model and GR.
5. If the true NMC signal is present but a standard-siren inference assumes GR, the inferred `H0` can be biased high by roughly `2.8 km s^-1 Mpc^-1` under a narrow prior and `5.9 km s^-1 Mpc^-1` under a wide prior in the paper's `c_M` comparison, comparable to the scale of the Hubble tension itself.
6. The paper also identifies a structural limitation of the simple `α_M ∝ Ω_Λ` phenomenological parameterization: the sign preferred by the NMC model can trigger `c_s^2 < 0` in that restricted parameterization, so model-agnostic EFT fits can misrepresent viable theory trajectories.

## Why this changes the picture

This materially extends the repository's earlier accepted result on non-minimal gravity easing cosmological tensions. That earlier entry established background-level Bayesian preference and a modified effective gravitational strength. The new result supplies a directly testable **propagation observable** and quantifies how assuming GR in standard-siren inference could bias `H0` by an amount comparable to the current discrepancy.

For modified-gravity model selection, this means cosmological tension relief and GW propagation can no longer be treated as separate validation channels. A viable model must fit the background and simultaneously predict a consistent `D_L^GW / D_L^EM(z)` trajectory. It also motivates model-specific standard-siren inference rather than relying only on rigid phenomenological templates.

For warp-adjacent research, the relevance is methodological rather than direct: any theory that changes the effective gravitational coupling or graviton propagation should be tracked through observable propagation functions, not just through local metrics or background equations.

## Scope / caveats

The current GWTC-5 constraints are not precise enough to distinguish this NMC prediction from GR. The analysis is therefore a consistency test and forecast-oriented observational discriminator, not a detection of modified gravity. A fully self-consistent joint cosmology + GW parameter fit for the model remains future work.

## Provenance

- arXiv abstract/HTML: https://arxiv.org/abs/2609.04112
- arXiv HTML: https://arxiv.org/html/2609.04112v1
- Submission date: 2026-09-03
- GWTC-5 modified-propagation posteriors are used by the authors as the current observational comparison set.

## Next verification question

Does a fully joint NMC fit to cosmological background data and GWTC-5 standard sirens, allowing the expansion history and GW-friction function to vary self-consistently, preserve the model's preference over GR/`ΛCDM` and the predicted negative `α_M` trajectory without prior-driven bias?

## QuantDeus roadmap relevance

No direct public-roadmap change. Provenance-linked takeaway for later integration: for modified-gravity / warp-adjacent candidates, track **background fit + propagation law + inference bias** together. Source: https://arxiv.org/abs/2609.04112
