# High-spin quadratic-gravity corrections to scalar quasinormal modes

## Decision
Accepted as a significant modified-gravity result.

## Classification
Simulation / model / strong-field modified gravity / black-hole spectroscopy / scalar–Gauss–Bonnet / dynamical Chern–Simons / high-spin quasinormal modes.

## Source quality
High. *Physical Review D* accepted the paper on 2026-09-03. The result is based on numerical rapidly rotating black-hole backgrounds and pseudo-spectral collocation rather than a low-order spin expansion. The observable calculated here is the spectrum of a massless minimally coupled **test scalar** on the modified backgrounds, not yet the full gravitational perturbation spectrum, so direct detector forecasts should remain conditional on that limitation.

## Primary sources
- APS accepted-paper record: https://journals.aps.org/prd/accepted/10.1103/jrnh-wsxw
- DOI: https://doi.org/10.1103/jrnh-wsxw
- arXiv: https://arxiv.org/abs/2604.02214
- Authors' accompanying numerical repository: https://github.com/StefHusken/scalar-QNMs-higher-derivative-gravity

## Core result
Previous quadratic-gravity QNM calculations were limited by spin-expanded backgrounds. Using recently constructed numerical black-hole solutions valid deep into the rapid-rotation regime, the authors compute leading scalar-QNM corrections in scalar Gauss–Bonnet (sGB) and dynamical Chern–Simons (dCS) gravity up to dimensionless spin `a/M = 0.99` with pseudo-spectral collocation. Reported numerical accuracy is better than approximately `10^-3` for the `l=m=0` mode and `10^-6` for higher multipoles.

For `a/M > 0.9`, corrections to some modes increase by **orders of magnitude**. The important change is therefore not merely an extended spin table: the near-extremal regime can qualitatively amplify beyond-GR spectral shifts and invalidate intuition extrapolated from moderate-spin calculations.

## Why this changes the picture
1. **High spin becomes a target-selection variable for modified-gravity spectroscopy.** Moderate-spin bounds cannot simply be extrapolated to near-extremal remnants; selected modes can become much more sensitive.
2. **Spin-expanded backgrounds are not sufficient in the most informative regime.** Reliable model selection near extremality requires numerical backgrounds and perturbation methods that remain valid at high spin.
3. **The enhancement is theory-comparative.** It appears in both parity-even sGB and parity-odd dCS examples, which suggests that rapid rotation itself can expose otherwise suppressed higher-curvature effects, although the precise mode dependence remains theory-specific.
4. **The result is complementary to previously accepted ringdown diagnostics.** The existing index contains differential hairy-black-hole ringdown tests and beyond-Horndeski primary-hair QNMs, but not this high-spin quadratic-curvature amplification result.

## Caveats
- The computed modes are for a massless minimally coupled test scalar, not the full coupled gravitational perturbation spectrum measured by GW detectors.
- The calculation is leading order in the higher-curvature coupling; very large apparent near-extremal corrections can signal a need to reorganize the perturbation expansion rather than a literal divergence of an observable.
- No modified-gravity detection is claimed.

## QuantDeus roadmap provenance note
This is relevant as a strong-field measurement-strategy update, not as a direct warp-engineering milestone. Provenance-linked takeaway: **when comparing sGB/dCS or other higher-curvature gravity against black-hole spectroscopy, prioritize rapidly rotating remnants and numerical high-spin backgrounds; moderate-spin QNM expansions can miss order-of-magnitude sensitivity changes close to extremality.** Source: https://doi.org/10.1103/jrnh-wsxw . No site change is warranted from this result alone.

## Next verification question
Do the **full gravitational** QNM sectors of rapidly rotating sGB and dCS black holes show the same near-extremal enhancement, and after imposing EFT-validity and realistic ringdown SNR, which modes retain a measurable gain over moderate-spin systems?
