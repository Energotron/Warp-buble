# Master screening equation for luminal Horndeski gravity

- **Run:** 2026-09-11 01:52 +03:00
- **Classification:** theory / model / nonlinear screening / luminal Horndeski / simulation tooling
- **Status:** accepted significant development
- **Source quality:** high — peer-reviewed *Physical Review D* article published 2026-09-09, with public symbolic and numerical implementations
- **Primary source:** https://doi.org/10.1103/tqp2-ccy5
- **Preprint:** https://arxiv.org/abs/2605.04154
- **Symbolic code:** https://github.com/sergisl/xAlpha
- **Numerical code:** https://github.com/sergisl/escut

## Result

Sirera, Baker, Hallam, and Naidoo derive the full unapproximated second-order cosmological perturbation equations for luminal Horndeski gravity in the EFT alpha basis, then systematically take the weak-field and quasistatic limits. For static spherical sources the nonlinear scalar sector reduces to a master screening equation whose operators classify which screening mechanism is active.

The framework recovers the familiar Vainshtein and chameleon regimes and identifies a distinct candidate regime, named **Phaedrus screening**, in which the screening radius scales linearly with source mass. The authors provide analytic and numerical solutions for the isolated mechanisms and release two public tools: `xAlpha`, which maps a luminal-Horndeski Lagrangian to perturbation coefficients, and `escut`, which solves the resulting nonlinear scalar boundary-value problem.

## Why this changes the picture

The important development is methodological. Screening is one of the main reasons cosmological modified-gravity models can evade Solar-System and compact-object bounds, but identifying the active nonlinear mechanism has often required bespoke derivations for each model. This work supplies a common equation and reproducible symbolic/numerical pipeline across a broad luminal-Horndeski class.

For the QuantDeus/Warp modified-gravity program this strengthens the **screening-first** gate. A model that looks interesting at background or linear-perturbation level should be mapped into the nonlinear master equation before phenomenological claims are promoted. The result also complements the existing two-scale sGB/Galileon report: rather than assuming one named screening mechanism, the active nonlinear operator can now be diagnosed directly from the Lagrangian in the supported theory class.

## Quality-gate interpretation

- This is a **theory/model/tooling** advance, not observational evidence for modified gravity.
- Phaedrus screening remains a **candidate regime**. Its physical viability is not established by the existence of a static solution alone; quasistatic validity and stability must still be checked.
- The published framework is limited to luminal Horndeski, scalar perturbations, second perturbative order, weak-field/quasistatic limits, and static spherical local sources. It is not yet a general DHOST/beyond-Horndeski or fully dynamical screening solver.
- Consistent with the repository's current gates, hyperbolicity/well-posedness and stability must be established before a screened branch is treated as predictive phenomenology.

## Public-roadmap relevance

**Provenance-linked takeaway:** screening in luminal Horndeski can now be treated as a reproducible model-classification step: map the Lagrangian with `xAlpha`, solve the nonlinear scalar master equation with `escut`, then require stability/well-posedness before using the screened branch for phenomenology. Provenance: https://doi.org/10.1103/tqp2-ccy5 , https://github.com/sergisl/xAlpha , https://github.com/sergisl/escut .

This is relevant to the QuantDeus research roadmap as a validation/toolchain improvement, not a direct warp-engineering milestone. No site change is warranted.

## Next verification question

Can the master-equation pipeline be extended beyond the static spherical quasistatic regime to time-dependent or nonspherical sources while preserving a demonstrable hyperbolic/well-posed evolution, and does the candidate Phaedrus regime survive that stronger test?
