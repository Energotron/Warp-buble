# Sound-horizon-free measurements recast the Hubble tension as a distance-ladder discrepancy

**Accepted:** 2026-09-03 16:19 +03:00  
**Classification:** Observational anomaly / cosmological model-selection constraint / Hubble tension / modified-gravity relevance  
**Source quality:** Peer-reviewed primary analysis — Physical Review D 114, 063507 (published 2026-09-03); arXiv:2601.00650  
**Significance:** high

## Development

Ioannis Pantos and Leandros Perivolaropoulos combine 88 determinations of the Hubble constant that do not use the sound horizon as a calibrated standard ruler. The sample is divided into distance-ladder measurements, local measurements that assume ΛCDM expansion, model-independent pure-local measurements, and CMB measurements constructed without sound-horizon information.

The principal result is that the discrepancy does not cleanly separate into an “early-Universe” and a “late-Universe” camp. Instead, the distance ladder sits high relative to the aggregate of all other sound-horizon-free methods:

```text
Distance ladder (30 measurements):
H0 = 72.73 ± 0.39 km s^-1 Mpc^-1

Distance-ladder-independent / sound-horizon-free (58 measurements):
H0 = 69.37 ± 0.34 km s^-1 Mpc^-1

Naive separation: 6.5σ
Conservative separation after modeled correlations: 3.9–4.3σ
```

The independent group is itself method-dependent. Local analyses assuming ΛCDM give `H0 = 67.61 ± 0.96`, pure-local model-independent measurements give `71.03 ± 0.69`, and CMB sound-horizon-free measurements give `69.07 ± 0.44 km s^-1 Mpc^-1`. The ΛCDM-assuming and model-independent subsets differ by about `3.4 km s^-1 Mpc^-1`, corresponding to an internal tension whose quoted significance depends on categorization.

## Why this clears the significance threshold

- It is a peer-reviewed synthesis of 88 measurements and isolates the disagreement without using the sound horizon, a common target of proposed early-time new physics.
- It materially changes the diagnostic question for modified-gravity and dark-energy solutions: changing pre-recombination physics or shrinking the sound horizon alone cannot explain why the distance ladder remains high relative to other sound-horizon-free methods.
- The result supplies a quantitative model-selection constraint rather than proposing another gravity parametrization.
- It leaves two sharply different interpretations: unrecognized distance-ladder systematics, or late-time/model-dependent physics that must reproduce the method-stratified pattern.

## Deduplication / comparison with prior accepted reports

The closest accepted cosmology report concerns Gen Ye's non-minimal gravity–matter coupling, which obtains `ln B = +12.1` for one specified data combination and predicts an early-Universe gravitational strength about 5% larger than today.

This result is independent and complementary. It does not fit a modified-gravity model and does not claim a detection of modified gravity. Instead, it reorganizes the observational anomaly across 88 sound-horizon-free determinations and therefore constrains which classes of proposed solutions remain diagnostically relevant. It is also distinct from the accepted kSZ force-law result, which directly measures the radial exponent of gravity on 30–230 Mpc scales.

## Relevance to warp / modified-gravity research

Cosmological modified-gravity sectors used to support unusual local curvature responses must be tested against more than a single combined `H0` likelihood. A viable theory must reproduce the separation between distance-ladder, pure-local, ΛCDM-conditioned, and CMB sound-horizon-free inferences without merely shifting the sound horizon.

The corresponding validation gate is:

```text
modified-gravity background
→ early-time sound-horizon effect
→ late-time expansion/growth effect
→ distance-ladder calibration
→ method-stratified H0 likelihoods
→ correlated-systematics robustness
```

The paper does not construct a warp metric, relax energy conditions, or establish modified gravity. Its value is as an observational filter on cosmological sectors that may accompany exotic-spacetime models.

## Confidence and limits

- **Classification:** observational anomaly / meta-analysis, not a detection of modified gravity.
- The journal publication is peer reviewed, and the accompanying analysis code and compilation are public.
- The quoted significance depends on assumptions about correlations among heterogeneous literature measurements; the conservative correlated estimate is 3.9–4.3σ rather than the naive 6.5σ.
- Categorization choices affect the internal discrepancy among distance-ladder-independent methods.
- Combining published point estimates cannot replace a joint reanalysis of the underlying likelihoods and shared calibration systematics.
- The result remains compatible with distance-ladder systematics; it does not uniquely require new cosmological physics.

## Primary sources

Ioannis Pantos and Leandros Perivolaropoulos, **“Dissecting the Hubble tension: Insights from a diverse set of sound-horizon-free H0 measurements,”** Physical Review D 114, 063507, published 3 September 2026.  
Journal: https://journals.aps.org/prd/abstract/10.1103/9pbn-13q8  
Preprint: https://arxiv.org/abs/2601.00650  
Analysis repository: https://github.com/ipantos/Dissecting-the-Hubble-Tension

## Publication-bridge decision

**Do not promote to Wix in this run.** This is a strong peer-reviewed cosmological diagnostic, but it does not establish modified gravity or directly change the QuantDeus Hundred-Year Plan. It belongs in the canonical evidence archive until a specific modified-gravity model independently explains the method-stratified pattern or the anomaly is resolved through a joint systematic analysis.
