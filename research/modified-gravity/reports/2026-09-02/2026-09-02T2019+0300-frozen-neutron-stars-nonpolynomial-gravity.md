# Frozen neutron stars in four-dimensional nonpolynomial gravity

- **Accepted by the watch:** 2026-09-02 17:19 UTC
- **Publication:** 2026-09-02
- **Authors:** Chen Tan; Yong-Qiang Wang
- **Journal:** *Physical Review D* **114**, 064007 (2026)
- **DOI:** https://doi.org/10.1103/jmnh-p43b
- **Primary preprint:** https://arxiv.org/abs/2512.23525
- **Classification:** Peer-reviewed theoretical construction with observationally constrained compact-star phenomenology
- **Framework:** Four-dimensional nonpolynomial quasi-topological higher-curvature gravity; its spherical sector is equivalent to a two-dimensional Horndeski theory

## Why this crosses the significance threshold

The paper identifies a qualitatively distinct, apparently equation-of-state-insensitive endpoint of neutron-star sequences in a singularity-resolving higher-curvature theory. Unlike routine mass-radius parameter scans, the endpoint develops an almost-null critical surface and becomes externally nearly degenerate with an extremal black hole. This creates a new compact-object/black-hole-mimicker channel for testing modified gravity.

This result is not duplicated by the existing archive entries on scalar-hairy black-hole stability, ringdown, EMRI fluxes, gravitational-wave propagation, laboratory torsion/nonmetricity bounds, cosmological force laws, or UV-locality. It adds an ordinary-matter stellar-equilibrium branch produced by an infinite higher-curvature tower.

## Core result

The action contains an infinite tower of nonpolynomial quasi-topological curvature terms,

```text
S = ∫ d^4x sqrt(-g) [c^3/(16πG)] [R + Σ_(n=2)^∞ α_n Z_(n)].
```

The authors solve the modified Tolman-Oppenheimer-Volkoff equations for three representative equations of state: BSk19, SLy4, and AP4. Increasing the modification parameter enlarges both stellar mass and radius. Above an equation-of-state-dependent critical central density, all three sequences enter a “frozen” state in which `1/g_rr` and `g_tt` approach zero extremely close to the surface. The critical horizon does not exactly coincide with the material boundary; a very thin matter layer remains outside it.

The endpoint is nearly indistinguishable from an extremal black hole to a distant observer and appears across all three equations of state. The construction can already occur at finite truncation (the paper gives `n = 3` as an example), so the phenomenon is not solely an artifact of retaining the complete infinite tower.

## Quantitative observational window

Mass-radius bands from PSR J0030+0451, PSR J0740+6620, and GW170817 still permit frozen-star formation in the explored models.

For `h(ψ) = ψ/(1 - α²ψ²)`, the reported observationally constrained upper values are approximately:

- BSk19: `α ≤ 0.9 × 10^8 m²`
- SLy4: `α ≤ 0.8 × 10^8 m²`
- AP4: `α ≤ 0.9 × 10^8 m²`

For `h(ψ) = ψ/sqrt(1 - α²ψ²)`:

- BSk19: `α ≤ 1.3 × 10^8 m²`
- SLy4: `α ≤ 1.1 × 10^8 m²`
- AP4: `α ≤ 1.2 × 10^8 m²`

Under the imposed causal-density cutoff, the frozen configurations lie on branches with `∂M/∂ρ_c > 0`, which is suggestive but not a substitute for a perturbative or nonlinear stability calculation.

## Technical significance

The work creates a falsifiable connection between a higher-curvature completion and compact-object observables:

1. modified TOV equilibrium and mass-radius curves;
2. an almost-null critical surface without an ordinary event horizon enclosing all matter;
3. black-hole-mimicker phenomenology;
4. prospective discrimination through tidal deformability, quasinormal spectra, and accretion-flow observables.

It also demonstrates that equation-of-state uncertainty does not obviously erase the endpoint within the three tested nuclear-matter models.

## Relevance to Warp Bubble Lab

For metric-engineering candidates built from nonpolynomial or resummed higher-curvature terms, acceptable vacuum solutions are not enough. The validation pipeline should now include:

```text
higher-curvature action
→ matter-coupled field equations
→ compact-star equilibrium sequence
→ critical-surface formation
→ causal-density cutoff
→ radial + nonradial stability
→ tidal/QNM/accretion discriminators
→ consistency with pulsar and binary-neutron-star data
```

The near-critical lapse behavior is especially relevant to any proposal that engineers extreme redshift surfaces: a geometry that looks horizonlike externally may hide a thin matter layer and may still fail dynamical stability.

## Confidence and limitations

- **Confidence:** High that the numerical equilibrium branch and reported mass-radius comparison are correctly represented; the work is peer reviewed.
- **Main limitation:** The paper does not provide a full radial, nonradial, or nonlinear stability analysis. The sign of `∂M/∂ρ_c` is only preliminary evidence.
- The result is model dependent and demonstrated in spherical symmetry.
- Rotation, merger dynamics, waveform systematics, tidal deformability, quasinormal modes, and accretion signatures remain to be calculated.
- Publication is a high-quality milestone, but it is not an observational detection of a frozen star.

## Deduplication note

The preprint first appeared on 2025-12-29 and the paper was accepted on 2026-07-13. This watch accepts the 2026-09-02 peer-reviewed publication as a previously unindexed milestone, not as a claim that the underlying numerical result was first released today.
