# SGWB modified-gravity forecasts: spectral-shape versus amplitude degeneracy

- Local acceptance time: 2026-09-09 01:29 +03:00
- Classification: simulation / observation-facing model test / stochastic gravitational-wave background / modified-gravity inference
- Status: accepted significant development
- Source quality: peer-reviewed accepted paper in Physical Review D (accepted 2026-09-03); technical manuscript arXiv:2607.05331; confidence high for the injection-recovery/model-selection result within the stated population model, medium for quantitative forecast transfer to real third-generation detector data

## Result

Rodrigo Fraga and Rafael C. Nunes perform joint injection-recovery forecasts for a compact-binary stochastic gravitational-wave background (SGWB) while varying both modified-gravity parameters and astrophysical population hyperparameters. They compare two beyond-GR channels: frequency-dependent waveform-generation corrections in the parametrized post-Einsteinian (ppE) framework and modified cosmological GW propagation encoded through a gravitational-wave luminosity distance different from the electromagnetic one.

The central result is a qualitative separation in identifiability. Frequency-dependent ppE corrections distort the **shape** of the SGWB spectrum and remain meaningfully constrainable with third-generation detectors, with the combined Cosmic Explorer + Einstein Telescope network performing best. Modified-propagation effects mainly rescale the **amplitude** smoothly and are recovered less accurately because they are more strongly degenerate with the binary-merger-rate normalization/evolution. In joint injections, the spectral-shape information survives, while amplitude-like modified-gravity parameters retain residual mutual and astrophysical degeneracies.

## Why this changes the picture

This upgrades the SGWB from a generic beyond-GR forecast channel into a more selective diagnostic: not all modified-gravity signatures should be treated as equally identifiable. A deformation that changes the frequency dependence can be separated from uncertain source populations more robustly than a propagation effect that behaves mainly as a broadband normalization shift.

For modified-gravity inference, the practical consequence is to prioritize observables that change spectral morphology and to treat smooth amplitude departures as population-model limited unless external astrophysical or cosmological information breaks the degeneracy. This complements resolved-event standard-siren and waveform tests by probing an integrated cosmological population rather than individual mergers.

## Sources

1. Physical Review D accepted paper (accepted 2026-09-03): Rodrigo Fraga and Rafael C. Nunes, *Modeling uncertainties in modified gravity predictions for the stochastic gravitational-wave background*. DOI: https://doi.org/10.1103/fftm-rssv
2. Technical manuscript: https://arxiv.org/abs/2607.05331

## Deduplication note

Not a duplicate of the existing NMC standard-siren/GW-friction entry. That report concerns modified luminosity-distance effects and H0 bias in resolved standard sirens. This work jointly models source-generation and propagation deviations in the unresolved compact-binary SGWB and demonstrates a detector-level identifiability hierarchy between frequency-dependent shape distortions and smooth amplitude rescalings under astrophysical population uncertainty.

## QuantDeus roadmap relevance

Provenance-linked takeaway for later integration: **in modified-gravity GW forecasts, rank spectral-shape distortions above smooth SGWB amplitude shifts as robust discriminants unless independent population information is available; amplitude-only departures should be flagged as astrophysical-degeneracy limited.** This is an inference/validation rule, not a website or engineering milestone.

## Next verification question

Does the shape-versus-amplitude identifiability hierarchy survive more flexible redshift-dependent merger-rate and mass-spectrum models, detector calibration/systematic uncertainties, anisotropic SGWB structure, and a full CE+ET cross-correlation likelihood with realistic foreground subtraction?