# GW250114 constraints on beyond-Teukolsky perturbation potentials

- **Run:** 2026-09-11 14:55 +03:00
- **Classification:** observation / interpretation / strong-field modified-gravity test / black-hole spectroscopy / theory-agnostic perturbation-equation constraints
- **Status:** accepted significant development
- **Source quality:** high — accepted by *Physical Review D* on 2026-09-10; analysis uses public LVK GW250114 ringdown/posterior products and an established beyond-Teukolsky parametrization
- **Primary source:** https://doi.org/10.1103/zzzw-vpgx
- **Preprint:** https://arxiv.org/abs/2607.26561

## Result

Völkel and Franchini apply the beyond-Teukolsky formalism directly to the high-SNR GW250114 black-hole ringdown and obtain the first observational bounds on theory-agnostic deviations at the level of the effective potential in the Teukolsky perturbation equation. The framework maps small potential deformations into shifts of the complex quasinormal-mode frequency, then constrains those deformations using public LVK information for the fundamental ringdown mode together with parametrized priors on the remnant mass and spin.

Across the tested deviation coefficients, the inferred departures remain consistent with the GR Teukolsky equation. The analysis is deliberately lightweight relative to a full theory-specific inspiral-merger-ringdown inference: it uses a simplified likelihood for the fundamental QNM, enabled by the event's high ringdown signal-to-noise ratio, while broadening remnant-parameter priors to probe sensitivity to theoretical systematics.

## Why this changes the picture

The repository already treats a calibrated test-scalar QNM shift as a useful low-cost **screening proxy** for deciding which beyond-Kerr models deserve a full gravitational perturbation calculation. This new result adds the complementary observational layer: one can now constrain generic perturbation-potential deformations directly from a real high-SNR event without first committing to a specific modified-gravity Lagrangian.

That creates a cleaner two-stage spectroscopy workflow for QuantDeus/Warp research:

1. use cheap scalar/QNM proxies to triage model space;
2. map surviving models into the gravitational perturbation sector and compare them against event-level beyond-Teukolsky constraints.

This does not turn a parameter-level null result into evidence for GR as a unique model, but it substantially improves the interface between model screening and data-facing black-hole spectroscopy.

## Quality-gate interpretation

- This is an **observation / interpretation** result, not a detection of modified gravity.
- The constraints are theory-agnostic at the perturbation-potential level; consistency of deviation coefficients with zero is a parameter-level statement, not proof that every alternative-gravity theory is excluded.
- The current implementation focuses on the fundamental QNM and a simplified likelihood, so full multimode and full Bayesian waveform analyses remain the stronger end-state for any specific theory.
- Remnant mass/spin information comes from LVK inspiral-merger-ringdown inference and is explicitly broadened to account for theoretical uncertainty; this is a useful robustness step but does not remove every waveform-model systematic.
- The result complements rather than replaces the repository's scalar-QNM shortcut: scalar proxies remain a screening tool, while beyond-Teukolsky event constraints provide a data-facing gate.

## Public-roadmap relevance

**Provenance-linked takeaway:** GW250114 now supports a practical event-level gate on generic black-hole perturbation-potential deviations: use beyond-Teukolsky constraints as the observational filter after cheap scalar/QNM model screening, and reserve full coupled gravitational calculations for models that survive both stages. Provenance: https://doi.org/10.1103/zzzw-vpgx and https://arxiv.org/abs/2607.26561 .

This is relevant to the QuantDeus research roadmap as a black-hole-spectroscopy validation step, not a direct warp-engineering milestone. No site change is warranted.

## Next verification question

How much do the GW250114 beyond-Teukolsky bounds tighten or rotate when multiple QNMs and deviation coefficients are inferred jointly with full Bayesian waveform systematics, and can specific sGB/dCS/Horndeski models be projected into that constrained potential basis without violating their own hyperbolicity/EFT-validity conditions?
