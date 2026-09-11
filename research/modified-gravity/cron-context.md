# Modified Gravity Watch Context

## Last accepted run
- Local time: 2026-09-11 14:55 +03:00
- Repository base before run: `d57df17c936e70b0ca90faa303e1d14f51e88e55`
- Latest accepted report commit: `1a4a597320a07365e97a4f0a80fc8ffc3badb622`
- Latest index commit: `032043c40a39a98c72e941a875bb2f2329b3720a`

## Accepted development
- Sebastian H. Völkel & Nicola Franchini — *Constraining deviations from the Teukolsky equation with GW250114*
- Classification: observation / interpretation / strong-field modified-gravity test / black-hole spectroscopy / theory-agnostic perturbation-equation constraints
- Status: accepted by *Physical Review D* on 2026-09-10; confidence high that the published analysis establishes the first event-level bounds on generic beyond-Teukolsky effective-potential deformations using public GW250114 ringdown products; confidence medium for translation into any specific alternative-gravity theory until model-specific mapping and full multimode/systematic inference are performed
- Key metric/structural result: tested beyond-Teukolsky deviation coefficients are consistent with zero; the method constrains generic perturbation-potential deformations from the fundamental QNM with remnant mass/spin priors broadened to probe theoretical uncertainty
- Primary source: https://doi.org/10.1103/zzzw-vpgx
- Preprint: https://arxiv.org/abs/2607.26561

## Relation to current quality gates
- Adds a **data-facing perturbation-equation gate** after the repository's calibrated scalar-QNM shortcut: cheap scalar/QNM calculations can screen model space, while surviving models should be projected into the gravitational perturbation sector and confronted with event-level beyond-Teukolsky constraints.
- Preserves the rule that the scalar-QNM shortcut is a screening proxy, not full gravitational proof.
- Preserves **model-level vs parameter-level separation**: deviation coefficients consistent with zero do not prove GR uniquely or exclude every modified-gravity model.
- Preserves **hyperbolicity/well-posedness first** for any specific theory mapped into the constrained potential basis; an observationally allowed deformation is not automatically a mathematically viable theory.
- Does not change the luminal-Horndeski screening pipeline, sGB hyperbolicity/scalar-charge bound, high-spin QNM target-selection anchor, or wide-binary forward-model/injection-recovery gate.

## Deduplication anchors
Previously accepted entries include: GW250114 beyond-Teukolsky event-level perturbation-potential constraints; luminal-Horndeski master screening equation plus `xAlpha`/`escut` and candidate Phaedrus screening; wide-binary 3D forward-model reanalysis removing the reported `gamma ~ 1.6` anomaly and tracing it to geometric de-projection; sGB minimum-mass/hyperbolicity cutoff plus bounded scalar charge; calibrated scalar-QNM proxy for beyond-Kerr gravitational ringdown plus ringdown/shadow complementarity; high-spin quadratic-gravity scalar-QNM amplification in sGB/dCS up to `a/M=0.99`; two-scale scalar–Gauss–Bonnet + cubic-Galileon near-horizon screening of scalar charge/dipolar emission and the resulting conditionality of GW dipole bounds; GW170817 multimessenger polarization-angle prior tightening extra-polarization bounds while Bayesian evidence favors GR; Schwarzschild–MOG small-scale precession constraint and resulting cross-scale running/screening requirement; scalar-charge memory / extra breathing-polarization memory from Ricci-coupled scalar–Gauss–Bonnet mergers; SGWB modified-gravity identifiability hierarchy; differential hairy-black-hole ringdown diagnostic; observer-robust warp-drive energy-condition certification / WarpAX v5; thermodynamic ghost-free higher-gradient Newtonian gravity; modified-entropic-gravity logarithmic weak-field tail; NMC standard-siren GW-friction signature; metric `f(R)` shear-free constraint-closure/GW-sector no-go; Gravity-from-Entropy FLRW tensor hyperbolicity obstruction; quadratic `f(R)` screened scalar-hair lensing cancellation; symmetric-teleparallel four-derivative ghost constraint; Galileon EFT nonlinear regularization/screening; sound-horizon-free Hubble-tension synthesis; ESGB cosmological constraint on hairy PBHs; nonpolynomial-gravity frozen neutron stars; GLPV static-hair stability obstruction; kSZ inverse-square force-law test; non-minimal gravity-matter coupling cosmology; stable cosmological cubic-Galileon hair; gravitational EFT UV locality; scalar fluxes for generic Kerr orbits; torsion/nonmetricity neutron-spin bounds; dCS pulsar-glitch birefringence; beyond-Horndeski primary-hair ringdown; curvature-coupled EMRI dephasing; wave-optics GW lensing in modified gravity; sGB gravitational memory.

## Public-roadmap relevance
Relevant as a strong-field validation pipeline improvement, not a direct warp-engineering milestone. Provenance-linked takeaway for later QuantDeus integration: **use GW250114 beyond-Teukolsky constraints as the event-level observational gate after cheap scalar/QNM screening; only models that survive both should justify expensive full coupled gravitational inference, and any model-specific projection must still satisfy its own hyperbolicity/EFT-validity conditions.** Sources: https://doi.org/10.1103/zzzw-vpgx and https://arxiv.org/abs/2607.26561 . No site change was made.

## Next verification question
How much do the GW250114 beyond-Teukolsky bounds tighten or rotate when multiple QNMs and deviation coefficients are inferred jointly with full Bayesian waveform systematics, and can specific sGB/dCS/Horndeski models be projected into that constrained potential basis without violating their own hyperbolicity/EFT-validity conditions?

## Next-run rule
Read this checkpoint plus the current `main` branch and `research/modified-gravity/INDEX.md` before searching. Fresh repository state has priority over this file. Reject duplicates, low-significance or preliminary preprints, cosmetic model variations, and results outside modified-gravity / warp-relevant gravity unless they materially change model selection, consistency conditions, observational strategy, or validated tooling.
