# Modified Gravity Watch Context

## Last accepted run
- Local time: 2026-09-10 12:14 +03:00
- Repository base before run: `5199b0239db48414927b395b04e9ff73510ffb01`
- Latest accepted report commit: `e5f106fd5e17b39c4d70d8e38c2aba739ed959b0`
- Latest index commit: `8dd9875d806d83ea0eafc0203ad9c1153ea66a60`

## Accepted development
- Saad & Ting — *No Gravitational Anomaly in Wide Binaries from Forward Modeling of 3D Orbits*
- Classification: observation / interpretation / weak-field modified-gravity test / wide binaries / MOND / hierarchical Bayesian inference
- Status: peer-reviewed publication in the *Open Journal of Astrophysics*; current arXiv version revised 2026-09-09; confidence high for the inference-method comparison on the studied 36-system sample, medium for generalization to the full wide-binary literature
- Core result: the same 36 wide binaries previously yielding `gamma = G_eff/G_N ~ 1.6` give `gamma = 1.00^{+0.24}_{-0.19}` when full 3D orbits are forward modeled with an independent semi-major axis. Replacing that treatment with geometric de-projection of projected separation recovers `gamma = 1.56^{+0.21}_{-0.18}`, identifying the separation-inference procedure as a concrete source of the apparent anomaly.
- Primary source: https://arxiv.org/abs/2603.11015
- Reproducibility/code: https://github.com/seratsaad/wb3d-gamma

## Deduplication anchors
Previously accepted entries include: wide-binary 3D forward-model reanalysis removing the reported `gamma ~ 1.6` anomaly and tracing it to geometric de-projection; sGB minimum-mass/hyperbolicity cutoff plus bounded scalar charge; calibrated scalar-QNM proxy for beyond-Kerr gravitational ringdown plus ringdown/shadow complementarity; high-spin quadratic-gravity scalar-QNM amplification in sGB/dCS up to `a/M=0.99`; two-scale scalar–Gauss–Bonnet + cubic-Galileon near-horizon screening of scalar charge/dipolar emission and the resulting conditionality of GW dipole bounds; GW170817 multimessenger polarization-angle prior tightening extra-polarization bounds while Bayesian evidence favors GR; Schwarzschild–MOG small-scale precession constraint and resulting cross-scale running/screening requirement; scalar-charge memory / extra breathing-polarization memory from Ricci-coupled scalar–Gauss–Bonnet mergers; SGWB modified-gravity identifiability hierarchy; differential hairy-black-hole ringdown diagnostic; observer-robust warp-drive energy-condition certification / WarpAX v5; thermodynamic ghost-free higher-gradient Newtonian gravity; modified-entropic-gravity logarithmic weak-field tail; NMC standard-siren GW-friction signature; metric `f(R)` shear-free constraint-closure/GW-sector no-go; Gravity-from-Entropy FLRW tensor hyperbolicity obstruction; quadratic `f(R)` screened scalar-hair lensing cancellation; symmetric-teleparallel four-derivative ghost constraint; Galileon EFT nonlinear regularization/screening; sound-horizon-free Hubble-tension synthesis; ESGB cosmological constraint on hairy PBHs; nonpolynomial-gravity frozen neutron stars; GLPV static-hair stability obstruction; kSZ inverse-square force-law test; non-minimal gravity-matter coupling cosmology; stable cosmological cubic-Galileon hair; gravitational EFT UV locality; scalar fluxes for generic Kerr orbits; torsion/nonmetricity neutron-spin bounds; dCS pulsar-glitch birefringence; beyond-Horndeski primary-hair ringdown; curvature-coupled EMRI dephasing; wave-optics GW lensing in modified gravity; sGB gravitational memory.

## Public-roadmap relevance
Relevant as a model-selection and validation-method gate, not a direct warp-engineering milestone. Provenance-linked takeaway for later QuantDeus integration: **treat low-acceleration wide-binary anomalies as inference-sensitive until the same systems survive full 3D orbital forward modeling and injection/recovery tests; 3D velocity data alone do not remove bias from reconstructing the unobserved orbital separation.** Sources: https://arxiv.org/abs/2603.11015 and https://github.com/seratsaad/wb3d-gamma . No site change was made.

## Next verification question
Does the disappearance of the `gamma ~ 1.6` boost persist in a substantially larger high-quality Gaia wide-binary sample when full 3D orbital forward modeling, unresolved-companion contamination, Galactic tides, and the MOND external-field effect are treated simultaneously under blinded injection/recovery tests?

## Next-run rule
Read this checkpoint plus the current `main` branch and `research/modified-gravity/INDEX.md` before searching. Fresh repository state has priority over this file. Reject duplicates, low-significance or preliminary preprints, cosmetic model variations, and results outside modified-gravity / warp-relevant gravity unless they materially change model selection, consistency conditions, or observational strategy.
