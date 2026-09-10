# Modified Gravity Watch Context

## Last accepted run
- Local time: 2026-09-11 01:52 +03:00
- Repository base before run: `3de446bbfdf87d55ce01ec4bdd6b90413d26dcfb`
- Latest accepted report commit: `b9dd7ac2975b353646575adbdbbc5a4b68b0eb56`
- Latest index commit: `8afac2c00340ecd2f9d748a96dead1350d8e7900`

## Accepted development
- Sirera, Baker, Hallam & Naidoo — *Master equation for screening in luminal Horndeski gravity*
- Classification: theory / model / nonlinear screening / luminal Horndeski / simulation tooling
- Status: peer-reviewed *Physical Review D* publication (published 2026-09-09); confidence high for the derivation/tooling within stated assumptions, low-to-medium for the physical viability of the newly identified Phaedrus regime pending stability and beyond-quasistatic tests
- Key metric/structural result: the static spherical weak-field/quasistatic scalar sector reduces to a common nonlinear master screening equation; Vainshtein and chameleon mechanisms are recovered, while a candidate Phaedrus regime has screening radius scaling linearly with source mass (`r_screen ∝ M`).
- Primary source: https://doi.org/10.1103/tqp2-ccy5
- Preprint: https://arxiv.org/abs/2605.04154
- Symbolic implementation: https://github.com/sergisl/xAlpha
- Numerical implementation: https://github.com/sergisl/escut

## Relation to current quality gates
- Extends the repository's **screening-first** anchor from individual models to a reproducible luminal-Horndeski classification pipeline.
- Complements the accepted two-scale sGB + cubic-Galileon result by requiring the active nonlinear screening operator to be diagnosed rather than assumed.
- Preserves the **hyperbolicity/well-posedness first** gate: a static screened solution, especially the candidate Phaedrus branch, is not treated as predictive until stability and dynamical well-posedness are established.
- Does not change the scalar-QNM screening role, high-spin QNM target-selection anchor, or wide-binary forward-model/injection-recovery gate.

## Deduplication anchors
Previously accepted entries include: luminal-Horndeski master screening equation plus `xAlpha`/`escut` and candidate Phaedrus screening; wide-binary 3D forward-model reanalysis removing the reported `gamma ~ 1.6` anomaly and tracing it to geometric de-projection; sGB minimum-mass/hyperbolicity cutoff plus bounded scalar charge; calibrated scalar-QNM proxy for beyond-Kerr gravitational ringdown plus ringdown/shadow complementarity; high-spin quadratic-gravity scalar-QNM amplification in sGB/dCS up to `a/M=0.99`; two-scale scalar–Gauss–Bonnet + cubic-Galileon near-horizon screening of scalar charge/dipolar emission and the resulting conditionality of GW dipole bounds; GW170817 multimessenger polarization-angle prior tightening extra-polarization bounds while Bayesian evidence favors GR; Schwarzschild–MOG small-scale precession constraint and resulting cross-scale running/screening requirement; scalar-charge memory / extra breathing-polarization memory from Ricci-coupled scalar–Gauss–Bonnet mergers; SGWB modified-gravity identifiability hierarchy; differential hairy-black-hole ringdown diagnostic; observer-robust warp-drive energy-condition certification / WarpAX v5; thermodynamic ghost-free higher-gradient Newtonian gravity; modified-entropic-gravity logarithmic weak-field tail; NMC standard-siren GW-friction signature; metric `f(R)` shear-free constraint-closure/GW-sector no-go; Gravity-from-Entropy FLRW tensor hyperbolicity obstruction; quadratic `f(R)` screened scalar-hair lensing cancellation; symmetric-teleparallel four-derivative ghost constraint; Galileon EFT nonlinear regularization/screening; sound-horizon-free Hubble-tension synthesis; ESGB cosmological constraint on hairy PBHs; nonpolynomial-gravity frozen neutron stars; GLPV static-hair stability obstruction; kSZ inverse-square force-law test; non-minimal gravity-matter coupling cosmology; stable cosmological cubic-Galileon hair; gravitational EFT UV locality; scalar fluxes for generic Kerr orbits; torsion/nonmetricity neutron-spin bounds; dCS pulsar-glitch birefringence; beyond-Horndeski primary-hair ringdown; curvature-coupled EMRI dephasing; wave-optics GW lensing in modified gravity; sGB gravitational memory.

## Public-roadmap relevance
Relevant as a validation/toolchain improvement, not a direct warp-engineering milestone. Provenance-linked takeaway for later QuantDeus integration: **for luminal Horndeski models, identify screening from the Lagrangian with a reproducible symbolic/numerical pipeline (`xAlpha` → master equation → `escut`) and require stability/well-posedness before promoting a screened branch to phenomenology.** Sources: https://doi.org/10.1103/tqp2-ccy5 , https://github.com/sergisl/xAlpha , https://github.com/sergisl/escut . No site change was made.

## Next verification question
Can the master-equation pipeline be extended beyond static spherical quasistatic sources to time-dependent or nonspherical configurations while preserving demonstrable hyperbolicity/well-posedness, and does the candidate Phaedrus screening regime survive that stronger test?

## Next-run rule
Read this checkpoint plus the current `main` branch and `research/modified-gravity/INDEX.md` before searching. Fresh repository state has priority over this file. Reject duplicates, low-significance or preliminary preprints, cosmetic model variations, and results outside modified-gravity / warp-relevant gravity unless they materially change model selection, consistency conditions, observational strategy, or validated tooling.
