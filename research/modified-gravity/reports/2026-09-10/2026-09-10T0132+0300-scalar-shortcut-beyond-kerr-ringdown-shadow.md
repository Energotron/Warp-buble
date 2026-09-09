# Scalar shortcut for beyond-Kerr ringdown tests and shadow complementarity

## Decision
Accepted as a significant modified-gravity result.

## Classification
Model / interpretation / strong-field modified gravity / black-hole spectroscopy / beyond-Kerr phenomenology / ringdown / black-hole imaging.

## Source quality
High. Peer-reviewed *Physical Review D* article published 2026-09-08. The method is benchmarked against cases where exact coupled gravitational-mode corrections are known (Kerr-Newman and Einstein-scalar–Gauss–Bonnet), then applied to phenomenological beyond-Kerr metrics. It is still an approximation: scalar-field QNM shifts are used as proxies for gravitational QNM shifts, so precision forecasts beyond the demonstrated tens-of-percent level require full perturbation calculations.

## Primary sources
- APS article: https://journals.aps.org/prd/abstract/10.1103/1xt4-xvtw
- DOI: https://doi.org/10.1103/1xt4-xvtw

## Core result
Pani and Sanna test a practical shortcut for theories/metrics where the full coupled gravitational perturbation problem is hard or unavailable: compute exact quasinormal modes of a test scalar on the modified black-hole background, then use the beyond-GR scalar-QNM shift as a proxy for the gravitational-QNM shift.

For Kerr-Newman and Einstein-scalar–Gauss–Bonnet black holes, the proxy reproduces known exact gravitational corrections, including mode-coupling effects, to within **tens of percent**. At current/near-term ringdown precisions of order percent-to-tens-of-percent, this is accurate enough to function as a screening tool and is typically comparable to or better than the usual eikonal extrapolation from photon-orbit properties.

Applied to a broad family of phenomenological metrics used in black-hole imaging tests, the method yields first scalar-QNM constraints for those spacetimes and shows that **current ringdown bounds are comparable to, and in some cases stronger than, black-hole shadow bounds**, while constraining parameter combinations that shadow observables alone do not access.

## Why this changes the picture
1. **A validated low-cost triage tool now exists for beyond-Kerr spectroscopy.** Full gravitational perturbation equations are not required before estimating whether a metric deformation is worth a full waveform calculation.
2. **Ringdown and shadow tests should be treated as complementary, not redundant.** They probe overlapping but non-identical combinations of the metric, so joint analyses can break degeneracies that either channel leaves open.
3. **The scalar proxy has empirical calibration against known beyond-GR examples.** This upgrades it from a heuristic to a quantitatively benchmarked approximation with a known error scale.
4. **This directly complements the repository's high-spin scalar-QNM result.** The previous accepted high-spin sGB/dCS study showed scalar QNMs can become strongly enhanced near extremality; this paper independently establishes when scalar-QNM deviations can serve as a useful proxy for the gravitational spectrum, while quantifying the approximation's limitations.

## Caveats
- The agreement is at the tens-of-percent level, not precision spectroscopy accuracy.
- The shortcut is validated only on tested examples; there is no guarantee for theories with qualitatively different perturbation content, strong extra-field resonances, parity mixing, or nonperturbative instabilities.
- Phenomenological metrics may not arise from a consistent covariant field theory.
- No evidence for a deviation from Kerr/GR is reported.

## QuantDeus roadmap provenance note
This is relevant as a **measurement-strategy / model-triage update**, not a warp-engineering milestone. Provenance-linked takeaway: **use scalar-QNM calculations as a calibrated first-pass filter for beyond-Kerr metrics before investing in full gravitational perturbation solvers, and pair ringdown with black-hole shadow constraints because the two channels probe complementary deformation directions.** Source: https://doi.org/10.1103/1xt4-xvtw . No site change is warranted from this result alone.

## Next verification question
How robust is the scalar-QNM proxy for rapidly rotating black holes and for theories with extra propagating fields/parity mixing, and can a joint ringdown+shadow Fisher/Bayesian analysis quantify where the combined constraints outperform either observable after realistic systematics are included?
