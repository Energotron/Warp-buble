# No gravitational anomaly in wide binaries under forward-modeled 3D orbits

- **Run:** 2026-09-10 12:14 +03:00
- **Classification:** observation / interpretation / weak-field modified-gravity test / wide binaries / MOND / hierarchical Bayesian inference
- **Status:** accepted significant development
- **Source quality:** high — peer-reviewed publication in the *Open Journal of Astrophysics*; current arXiv version revised 2026-09-09
- **Primary source:** https://arxiv.org/abs/2603.11015
- **Reproducibility/code:** https://github.com/seratsaad/wb3d-gamma

## Result

Saad and Ting reanalyze the same 36 wide-binary systems for which Chae et al. reported a low-acceleration gravity boost of roughly `gamma = G_eff/G_N ~ 1.60`. Instead of geometrically de-projecting the observed projected separation and using that as the three-dimensional separation proxy, they fit a hierarchical Bayesian orbit model with an independent semi-major axis and forward-project the full three-dimensional orbits into observable space.

With that forward model they obtain `gamma = 1.00^{+0.24}_{-0.19}`, consistent with Newtonian gravity. As a diagnostic, replacing the independent semi-major-axis treatment with a geometric de-projection of the observed projected separation recovers `gamma = 1.56^{+0.21}_{-0.18}`, close to the previously reported anomaly.

The important development is therefore not simply another null wide-binary result: the analysis identifies a concrete inference choice that can reproduce the anomalous boost on the same dataset.

## Why this changes the picture

Wide binaries are attractive low-acceleration gravity laboratories because they probe accelerations near the MOND scale without invoking galactic dark-matter distributions. The 36-system 3D-velocity sample had been especially interesting because its reported anomaly was advertised as less vulnerable to projection systematics.

This reanalysis weakens that interpretation. It shows that having three-dimensional velocity information does not by itself eliminate geometric inference bias: the treatment of the unobserved orbital separation and orbital elements remains decisive. A claimed gravity boost from a small high-quality sample should therefore pass a forward-model/injection-recovery gate before it is promoted as evidence for modified gravity.

For the QuantDeus modified-gravity program, this complements the existing kSZ inverse-square test and other weak-field constraints by sharpening the methodology for local low-acceleration anomalies. It does not rule out MOND or every wide-binary anomaly claim; it specifically removes the evidential force of this 36-pair result under the authors' hierarchical model and identifies the source of the discrepancy.

## Caveats

- The sample contains only 36 systems, so the uncertainty on `gamma` remains broad.
- This result addresses the specific 3D wide-binary analysis and its inference geometry; it is not a universal adjudication of all Gaia wide-binary studies.
- Different sample selections, contamination models, external-field treatments, and orbital priors can still matter and require independent cross-checks.

## Public-roadmap relevance

**Provenance-linked takeaway:** treat low-acceleration wide-binary anomalies as inference-sensitive until the same systems survive full three-dimensional orbital forward modeling and injection/recovery tests. Provenance: https://arxiv.org/abs/2603.11015 and https://github.com/seratsaad/wb3d-gamma .

This is a model-selection / validation-method update, not a direct warp-engineering milestone. No site change is warranted.

## Next verification question

Does the disappearance of the `gamma ~ 1.6` boost persist in a substantially larger high-quality Gaia wide-binary sample when the full 3D forward model, unresolved-companion contamination, Galactic tides, and MOND external-field effect are treated simultaneously under blinded injection/recovery tests?
