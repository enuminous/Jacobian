# Zoo operation ledger

All 52 source-inventory entries are included. Entry numbers below identify inventory rows, not new historical animal numbers. Five source operators ran; 47 are UNRESOLVED for absent inputs or definition. PASS/FAIL names the bounded target property, not the success of running the code.

Definitions come from the pinned inventory and Monolithic-Zoo-Lean4 coverage. The full input, transform, criterion and output records are in [roster.json](roster.json). No arbitrary confidence values or feature scores are supplied.

## 1. Tortoise — UNRESOLVED

**Operation:** ordered split; temporal separation contract; Brier gain

**Inputs:** No timestamped labeled predictions, temporal split, Brier outcomes or matched forecasting control.

**Transformation:** M1 recursion input: sₜ⁽⁰⁾ = (Cₜ, ΔCₜ, Δ²Cₜ); sₜ⁽ᵏ⁺¹⁾ = ½sₜ⁽ᵏ⁾ + ½tanh(sₜ⁽ᵏ⁾ + rₜ₋₁); k=0,1,2; rₜ=sₜ⁽³⁾

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Tortoise/blob/6658128fd2df96ff6c32fce219bfc9ee3e8876da/model_full.py) · [Audit evidence](PROTOCOL.md)

## 2. Owl — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** zₜ=(xₜ−med_w(x))/(1.4826·MAD_w(x)+ε); owl_warningₜ = mean(rankₚ(componentₜ))

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Owl/blob/afe43985e76e74e65ff76e64b4c753eab11f1abc/signals.py) · [Audit evidence](PROTOCOL.md)

## 3. Octopus — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** gₜ = graph + local relational features; latentₜ = meanⱼ(rankₚ(gₜⱼ))

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Octopus/blob/e590a6d9d757357da72f043facc62e22d40df45e/latent_state.py) · [Audit evidence](PROTOCOL.md)

## 4. Gecko — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** corr_lossᵢⱼ = 1−|corr_w(xᵢ,xⱼ)|; gradient_lossₜ = max(0, Δcoherence_lossₜ)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Gecko/blob/0345f2ed1d98c15306312c828cfe68e6fa8c5c2e/features.py) · [Audit evidence](PROTOCOL.md)

## 5. Hive — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** deliveryₜ=(overdue+blocked+reopen+handoff)/4; hive_riskₜ = meanⱼ(rankₚ(componentₜⱼ))

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Hive/blob/e66e03d67c19f1f1e663a2a7feaea9f21c48384e/features.py) · [Audit evidence](PROTOCOL.md)

## 6. Eagle — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** gradient_loss=(rank(anomaly)+rank(|Δx|)+rank(|Δ²x|)+rank(disagreement)+rank(sign conflict))/5; eagle_riskₜ = meanⱼ(rankₚ(componentₜⱼ))

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Eagle/blob/d4f6fb0293129de8850fa15667b75aaaa7cc5339/features.py) · [Audit evidence](PROTOCOL.md)

## 7. Crab — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** rₜ=xₐ−x_b; contradictionₜ=|rₜ−med_w(r)|/(1.4826·MAD_w+ε); crab_scoreₜ = rank-aggregate(contradiction, velocity, consensus instability)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Crab/blob/f49f430353c954f54567e754b9bea60b26c40732/features.py) · [Audit evidence](PROTOCOL.md)

## 8. Shepherd — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** errorₜ=(step+tool+repeat+contradiction+memory+unresolved)/6; hazardₜ = meanⱼ(rankₚ(error, recovery deficit, stall, recurrence, drift))

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Shepherd/blob/c875bad6c5185cc3d5813fb097e5ccc2c27b5234/features.py) · [Audit evidence](PROTOCOL.md)

## 9. Pulse — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** safetyₜ=(critical miss+unsafe+abstention+repeat failure)/4; pulse_riskₜ = meanⱼ(rankₚ(uncertainty, review, safety, shift, history))

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Pulse/blob/78b7bd4a4fa1597373e184fbe895a513574c8939/features.py) · [Audit evidence](PROTOCOL.md)

## 10. Cat — UNRESOLVED

**Operation:** ablation penalty and sign classifier; exact-integer sign reference

**Inputs:** No fitted feature-family model, held-out Brier scores or controlled feature ablations.

**Transformation:** coherenceₜ = meanⱼ exp(−contradictionₜⱼ); sₜ⁽ᵏ⁺¹⁾=½sₜ⁽ᵏ⁾+½tanh(sₜ⁽ᵏ⁾+rₜ₋₁), k=0,1,2

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Cat/blob/9bf56f891b3ac22e38089ade0351852df1670d11/features.py) · [Audit evidence](PROTOCOL.md)

## 11. Fox — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** feedbackₜ = mean₍a≠b,ℓ₎ |corr_w(xₐ,t, x_b,t−ℓ)|; fox_riskₜ = meanⱼ(rankₚ(feedback, oscillation, damping, overshoot))

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Fox/blob/b4c317d45b7f2b69e92a657ba8d9ccdb4977a457/features.py) · [Audit evidence](PROTOCOL.md)

## 12. Spider — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** rₜ=x_up−x_down(t−ℓ); stressₜ=w·|rₜ−med_w(r)|/(1.4826·MAD_w+ε); network stress aggregates edge mean, peak, concentration, velocity

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Spider/blob/fd8f546d528f0c740248baddd6f0ea05e60abc25/features.py) · [Audit evidence](PROTOCOL.md)

## 13. Raven — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** residualₜ = observedₜ − linear_predictionₜ; residual features = mean(|e|), variance(e), Δmean(|e|), lag-1 corr(e)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Raven/blob/d18b4a8e05812ea3d577aa63643071c09fad3ea9/features.py) · [Audit evidence](PROTOCOL.md)

## 14. Dolphin — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** rₜ=x_target−x_source(t−ℓ); zₜ=|rₜ−med_w(r)|/(1.4826·MAD_w+ε); latent velocityₜ=Δ(mean relational residual); accelerationₜ=Δvelocityₜ

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Dolphin/blob/718b09ca4966d76e186cda7971d09be2caa39321/features.py) · [Audit evidence](PROTOCOL.md)

## 15. Ant — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** local risk=(rank(deficit)+rank(lead)+rank(backlog)+substitution deficit)/4; edge pressureₜ = w·risk_upstream(t−ℓ)+|w·risk_upstream−risk_downstream|

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Ant/blob/e7432f132a47804626322ba7343d187bd2425a75/features.py) · [Audit evidence](PROTOCOL.md)

## 16. Moth — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** recurrenceₜ,ℓ = exp(−|dₜ−dₜ₋ℓ|/(rolling σₜ+ε)); oscillation power from detrended periodogram; growthₜ=max(0, Δpowerₜ)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Moth/blob/08e5ce7cf219f6009b446829110c3399b658a5bd/features.py) · [Audit evidence](PROTOCOL.md)

## 17. Shark — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** mismatch=(rank(speed)+rank(heading)+rank(steering)+rank(lateral error))/4; hₜ⁽ᵏ⁺¹⁾=½hₜ⁽ᵏ⁾+½tanh(hₜ⁽ᵏ⁾+hₜ₋₁); k=0,1,2

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Shark/blob/13ef3943eb389a157f214fc4db054e926b22aa5a/features.py) · [Audit evidence](PROTOCOL.md)

## 18. Penguin — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** SNRₜ=meanᵢ|xᵢₜ|/(√meanᵢ Var_w(xᵢ)+ε); noise_scoreₜ = meanⱼ(rankₚ(noise, instability, entropy, drift, 1/SNR))

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Penguin/blob/1a99e0c1eb1c6902d2909721aae9ac8e76bfb75e/features.py) · [Audit evidence](PROTOCOL.md)

## 19. Bat — UNRESOLVED

**Operation:** verdict kernel with source placebo precedence; fitting excluded

**Inputs:** No paired prediction losses, placebo comparison or prospective outcome series.

**Transformation:** ΔBrier = Brier(control) − Brier(candidate); positive ΔBrier favors candidate; compare matched baselines and placebos

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Bat/blob/67c2c0e3cd6fb035a0e47862ec3f7e64729fa92d/bat.py) · [Audit evidence](PROTOCOL.md)

## 20. Hedgehog — UNRESOLVED

**Operation:** generalization verdict and environment separation obligation; training excluded

**Inputs:** No held-out environment outcomes or trained-model generalization data.

**Transformation:** relational energyₜ = meanᵢ(xᵢₜ − meanⱼxⱼₜ)²; pₜ = 0.65pₜ₋₁ + 0.35tanh(mean(rank(disagreement, change, energy)) + pₜ₋₁)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Hedgehog/blob/2e9b46039a6422961f9f08fb6457e2634a4c1de4/features.py) · [Audit evidence](PROTOCOL.md)

## 21. Crocodile — UNRESOLVED

**Operation:** difference-in-differences kernel and conditional identification contract

**Inputs:** No treatment/control time series or causal identification assumptions.

**Transformation:** Yₜ₊ₕ = α + ΣℓβℓTₜ₋ℓ + γYₜ + εₜ; causal estimate = treatment coefficient βℓ with lagged downstream state

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Crocodile/blob/2407241cc2d77f58bc044f9be6bff8ceb5c0b55a/crocodile.py) · [Audit evidence](PROTOCOL.md)

## 22. Dragon — UNRESOLVED

**Operation:** rank aggregation of precomputed component columns; feature extraction and model training not ported

**Inputs:** No measured multichannel time series or precomputed domain feature columns; rank aggregation has no valid Jacobian audit input.

**Transformation:** escapeₜ=(rank(distance)+rank(velocity)+rank(direction change)+1−rank(regime margin))/4; aₜ=0.7aₜ₋₁+0.3tanh(baseₜ+aₜ₋₁); base=mean(near, persistence, direction stability)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Dragon/blob/9ac2ffe7a271e5375b3bb5a2e6936c822fcc711f/features.py) · [Audit evidence](PROTOCOL.md)

## 23. Turtle — UNRESOLVED

**Operation:** summary verdict and veto precedence; group normalization supplied

**Inputs:** No independent effect estimates with calibrated provenance weights for meta-analysis.

**Transformation:** wᵢ = clip(confidenceᵢ)·clip(provenanceᵢ)·replicationᵢ; effectᵢ = tanh(raw effectᵢ / scale); group-adjust before synthesis

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Turtle/blob/ff98950fcb40f8a8c151a5c9466d11a240146beb/normalize.py) · [Audit evidence](PROTOCOL.md)

## 24. Magpie — UNRESOLVED

**Operation:** groundedness and history-dependent alarm; entropy/storage excluded

**Inputs:** No calibrated support/inference scores or prior groundedness history; scores are not invented from prose.

**Transformation:** groundedness=(support+provenance+corroboration)/(support+provenance+corroboration+inference+unresolved+contradiction+ε); alarm if clipped(coherence)−groundedness>θ and groundedness is falling

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Magpie/blob/342438c179832be2fe8b6dbdf1b4b5b0097df2ce/magpie.py) · [Audit evidence](PROTOCOL.md)

## 25. Wolf — UNRESOLVED

**Operation:** local channel contribution, weight, EMA and alarm contract; graph aggregation supplied

**Inputs:** No measured precursor channels, calibrated uncertainty or EMA history.

**Transformation:** local=max(0, α·hazard_z + β·Δhazard_z − γ·uncertainty); Pₜ=ρPₜ₋₁+(1−ρ)·weighted_mean(local channel scores)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Wolf/blob/7e4fd6d2b7c8829138a5f2d58f1b4cf39ed208c4/wolf.py) · [Audit evidence](PROTOCOL.md)

## 26. Elephant — PASS

**Operation:** active-event filter and fuel-bounded lineage abstraction; full memory API excluded

**Inputs:** Archive → CI → audit event records; provenance strings from source/CI IDs.

**Transformation:** order fidelity=correct expected event-order pairs / comparable pairs; drift=1−(order fidelity+status fidelity+provenance fidelity)/3

**Criterion:** Preserve event order and provenance strings.

**Output:** Recorded event order and provenance; retention metric excluded. Execution: pinned Python source executed.

[Source definition](https://github.com/enuminous/Elephant/blob/a30bd9ae77d7df31f35b533e5310eb7e06aa3d40/elephant.py) · [Audit evidence](evidence/checks.json)

## 27. Chameleon — UNRESOLVED

**Operation:** unexplained/noise-adjusted excess; supplied centroid distances

**Inputs:** No context embeddings, centroid distances or within-context noise sample.

**Transformation:** between=mean pairwise distance(context centroids); noise-adjusted divergence=max(0, between−mean within-context distance)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Chameleon/blob/75095bd9834953d52a88fd8c64f75393e15d880f/chameleon.py) · [Audit evidence](PROTOCOL.md)

## 28. Jellyfish — UNRESOLVED

**Operation:** dynamic edge weight, flow, next health and harm; graph aggregation supplied

**Inputs:** No measured stress-dependent graph, node health or degradation transitions.

**Transformation:** wᵢⱼ=max(0, base weightᵢⱼ + stress gainᵢⱼ·stress)·confidenceᵢⱼ; degradation′ᵢ=clip(degradationᵢ+α·Σⱼwⱼᵢ·degradationⱼ)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Jellyfish/blob/7119a66a75092354deee27dcb89f1d20add4e4e6/jellyfish.py) · [Audit evidence](PROTOCOL.md)

## 29. Beaver — UNRESOLVED

**Operation:** acceptance contract including bounds and rollback flags; external repair not certified

**Inputs:** No applied repair with before/after performance, collateral metrics and rollback measurement.

**Transformation:** effectiveness=target_before−target_after; net repair value=effectiveness−Σₖ collateral_weightₖ·max(0,afterₖ−beforeₖ)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Beaver/blob/f6255d49e71e31c325d474039d4e01163266608b/beaver.py) · [Audit evidence](PROTOCOL.md)

## 30. Mantis — UNRESOLVED

**Operation:** calibrated z-score aggregation and state decision; baseline fitting supplied

**Inputs:** No baseline-calibrated variance, autocorrelation and curvature series.

**Transformation:** precursor=mean(max(0,z_variance), max(0,z_AC1), max(0,z_curvature)); alarm if precursor≥threshold and fraction of positive z scores≥min_coherence

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Mantis/blob/a9fd85eb62a22d3667201dd6747bf8d296ad9083/mantis.py) · [Audit evidence](PROTOCOL.md)

## 31. Bison — UNRESOLVED

**Operation:** single-component queue transition; exact natural-number capacity bound

**Inputs:** No service demand, capacity and queue transition data.

**Transformation:** queue′=min(queue_limit,max(0,queue+demand−served)); qraw=max(0,q+d−served); dropped=max(0,qraw−q_limit); q′=min(qraw,q_limit)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Bison/blob/588acafecff764cb417637861d6d9a1e6bdf502f/bison.py) · [Audit evidence](PROTOCOL.md)

## 32. Weasel — FAIL

**Operation:** bounded finding filter; target search/enumeration remains external

**Inputs:** Actual baseline parser; fixed malformed text alternatives; max_changes=1.

**Transformation:** severity=max(0, weakness_predicate(target(perturbed_input))); rank counterexamples by severity ↓, change cost ↑, reproducibility ↓

**Criterion:** Every invalid report must be rejected; any reproducible false accept fails target.

**Output:** Four counterexamples, each reproduced in three of three trials. Execution: pinned Python source executed.

[Source definition](https://github.com/enuminous/Weasel/blob/fa2d91ae108f6b3bb515fb16ff0c22ae02324b06/weasel.py) · [Audit evidence](evidence/checks.json)

## 33. Salmon — PASS

**Operation:** unresolved-mass kernel and fuel-bounded trace abstraction; weighted tracing excluded

**Inputs:** Report → CI → archive chain with documented unit bookkeeping edges.

**Transformation:** origin contribution += path_weight·confidence·provenance_quality; origin entropy=−Σₒpₒlog(pₒ), pₒ=contributionₒ/Σ contribution

**Criterion:** Trace must terminate at the recorded archive and expose shared origin.

**Output:** One origin, depth two, no missing chain edge; not an independence score. Execution: pinned Python source executed.

[Source definition](https://github.com/enuminous/Salmon/blob/b141f6ccd5b0e789ceddaa91ec9e664cd02c4981/salmon.py) · [Audit evidence](evidence/checks.json)

## 34. Orca — UNRESOLVED

**Operation:** handoff checks and aggregate coordination formula; pairwise metrics supplied

**Inputs:** No agent handoff records or measured shared-state distances.

**Transformation:** state consistency=1/(1+mean pairwise shared-state distance); coordination=0.30s+0.30h+0.20(1−conflict)+0.10(1−ambiguity)+0.10(1−lag)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Orca/blob/a5caecf5a81b05495904528b0135fd272daaf90e/orca.py) · [Audit evidence](PROTOCOL.md)

## 35. Mole — UNRESOLVED

**Operation:** observability gap and coverage-gated hidden-failure flag; indicators supplied

**Inputs:** No calibrated surface-health and deep-indicator measurements or coverage denominator.

**Transformation:** latent degradation=Σᵢnormalized_weightᵢ·deep_indicatorᵢ; observability gap=max(0, latent degradation−surface degradation)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Mole/blob/523f8017851070f2c5d0249da4601357b24dda24/mole.py) · [Audit evidence](PROTOCOL.md)

## 36. Lynx — UNRESOLVED

**Operation:** novelty, yield and emergence contract; reference distances supplied

**Inputs:** No validated reference-distance/rarity metric or replication/yield data; literature discussion is separate.

**Transformation:** novelty=max(0, α·distance+β·rarity−γ·rediscovery similarity); latent yield=novelty·replication·yield

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Lynx/blob/d2f705136a616190f2c135ec9fa0df57b5c34020/lynx.py) · [Audit evidence](PROTOCOL.md)

## 37. Horse — UNRESOLVED

**Operation:** trust/workload/joint-effectiveness kernels and handoff contract

**Inputs:** No human workload, trust calibration, handoff or joint-performance observations.

**Transformation:** trust error=|human trust−system reliability|; workload penalty=min(1, overload+½(1−attention)+½fatigue); joint=clip(0.35 success+0.20 handoff+0.20(1−trust error)+0.15(1−workload)+0.10·(quality+1)/2−0.05·latency)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Horse/blob/e55b6881a1d3a0e10fb32e474a3612aa4bf0ab69/horse.py) · [Audit evidence](PROTOCOL.md)

## 38. Termite — UNRESOLVED

**Operation:** agent update and synchronous mapping; graph weighted inputs supplied

**Inputs:** No interacting agent state network with influence parameters.

**Transformation:** targetᵢ=Σⱼwᵢⱼsⱼ/Σⱼwᵢⱼ; s′ᵢ=clip((1−χᵢ)sᵢ+χᵢtargetᵢ+biasᵢ)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Termite/blob/76f70136ebf3b9e8bf4f38d971cce07cb2e73b0f/termite.py) · [Audit evidence](PROTOCOL.md)

## 39. Phoenix — UNRESOLVED

**Operation:** recovery completeness and hold-window predicate; fidelity inputs supplied

**Inputs:** No recovery experiment with reference state, invariant and capability trajectories.

**Transformation:** fidelity=max(0,1−√mean((state−reference)²)); recovery=0.40·fidelity+0.30·invariants passed+0.30·capability score

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Phoenix/blob/20079489fe4c180105d43b4382733a5506e27beb/phoenix.py) · [Audit evidence](PROTOCOL.md)

## 40. Cobra — UNRESOLVED

**Operation:** persistent/proxy divergence and risk kernels; deltas supplied

**Inputs:** No paired proxy and persistent-objective trajectories.

**Transformation:** Dₜ=ρDₜ₋₁+(1−ρ)objective divergenceₜ; risk=clip((w_DD+w_Vviolation+w_Pproxy divergence+w_Ccontext gap)·evidence confidence)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Cobra/blob/1af3a2016813a04a414be3c79a2b40b158154783/cobra.py) · [Audit evidence](PROTOCOL.md)

## 41. Whale — UNRESOLVED

**Operation:** cumulative deviation, history gap and stability formula; slope supplied

**Inputs:** No long-horizon deviation/history series or predeclared stability threshold.

**Transformation:** penalty=0.30·scaled|global drift|+0.25·scaled cumulative deviation+0.25·scaled recency gap+0.20·scaled regime memory; stability=max(0,1−penalty)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Whale/blob/c64bbfb54fce0d4dba2eb3d9a285bba7c7605d39/whale.py) · [Audit evidence](PROTOCOL.md)

## 42. Falcon — UNRESOLVED

**Operation:** latency/missed/reaction-margin kernel; streaming threshold monitor excluded

**Inputs:** No event arrival, detection latency and intervention deadline dataset.

**Transformation:** zₜ=|yₜ−meanₜ₋₁|/(stdₜ₋₁+ε); scoreₜ=ρ·scoreₜ₋₁+(1−ρ)zₜ; alarm if score≥threshold

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Falcon/blob/bf74635c358b997983a3ee19a4e7c9bd23bc8436/falcon.py) · [Audit evidence](PROTOCOL.md)

## 43. Rhino — UNRESOLVED

**Operation:** retention, amplification and graceful-failure kernels; invariants supplied

**Inputs:** No operational retention/amplification sequence with supplied invariants.

**Transformation:** loss=1−(0.5·performance retention+0.5·structural retention); shock amplification=loss/shock magnitude; retain invariants separately

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Rhino/blob/8718a3132ffc46ec46564fc0d4fd086637235cca/rhino.py) · [Audit evidence](PROTOCOL.md)

## 44. Bonobo — UNRESOLVED

**Operation:** gain, exploitation and cooperation score; dispersion supplied

**Inputs:** No multi-agent gains, exploitation penalties or cooperation experiment.

**Transformation:** gainᵢ=utilityᵢ−baselineᵢ; fairness=1/(1+variance(normalized gains)); cooperation=weighted efficiency+stability+fairness+(1−exploitation)+resolution

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Bonobo/blob/40a3c44a997b5e66ebb2c2dbae4d33ce779e630a/bonobo.py) · [Audit evidence](PROTOCOL.md)

## 45. Axolotl — UNRESOLVED

**Operation:** recovery, efficiency and resilience; transformation/invariants supplied

**Inputs:** No measured transformation/recovery efficiency and resilience experiment.

**Transformation:** recovery=(adapted function−damaged function)/(reference−damaged); resilience=0.45 recovery+0.30 invariants+0.15 efficiency+0.10 useful transformation

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Axolotl/blob/af8e011f0be6f5852b3d102d4004aaf86e2bcfd4/axolotl.py) · [Audit evidence](PROTOCOL.md)

## 46. Butterfly — UNRESOLVED

**Operation:** layer update, amplification and bounded trajectory; graph comparison excluded

**Inputs:** No layered dynamical graph or perturbed trajectory dataset.

**Transformation:** incomingᵢ=Σⱼwᵢⱼ·stateⱼ; state′ᵢ=clip(baseᵢ+incomingᵢ+gainᵢ·max(0,stateᵢ−thresholdᵢ)²)

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Butterfly/blob/5952c7f260f65835e1a67d4502aac1e4015bfe49/butterfly.py) · [Audit evidence](PROTOCOL.md)

## 47. Harlequinn — UNRESOLVED

**Operation:** N/A — no source equation or implementation to verify

**Inputs:** The source inventory explicitly records that no operation definition or implementation exists.

**Transformation:** N/A — repository README provides a name only; no species/operation definition; N/A — no source equation or implementation to verify

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Harlequinn/blob/df38b3c01b7fe54592b53a1b96013bbcf6c0914b/README.md) · [Audit evidence](PROTOCOL.md)

## 48. woodpecker — UNRESOLVED

**Operation:** necessary if loss>max(ε,|baseline|·(1−contribution fraction)); redundant if loss≤ε

**Inputs:** No registered predictive-model ablation experiment; code rejection tests are not substituted for its contribution metric.

**Transformation:** loss=oriented baseline−oriented ablation; necessary if loss>max(ε,|baseline|·(1−contribution fraction)); redundant if loss≤ε

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/woodpecker/blob/d281b313020cfef0183a883746aaa3ff4caafbfa/woodpecker/core.py) · [Audit evidence](PROTOCOL.md)

## 49. Chimera — UNRESOLVED

**Operation:** D tag=not operationally recoverable AND evidence is sufficient; U when evidence is insufficient

**Inputs:** No physical event/key/recovery-map record; a Lean theorem is not relabeled as a quantum/classical event.

**Transformation:** K tag=identifiable key AND explicit recovery map; D tag=not operationally recoverable AND evidence is sufficient; U when evidence is insufficient

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Chimera/blob/b5e35e71d6454462e0da24d8bb2ea90e80520471/chimera.py) · [Audit evidence](PROTOCOL.md)

## 50. Nightengale — UNRESOLVED

**Operation:** effectₖ=center(cumulative sum of ALEₖ), weighted by bin counts

**Inputs:** No fitted prediction function, explanatory dataset or ALE/tree stopping inputs.

**Transformation:** ALEₖ=meanᵢ[f(xⱼ=upperₖ,x₋ⱼ)−f(xⱼ=lowerₖ,x₋ⱼ)]; effectₖ=center(cumulative sum of ALEₖ), weighted by bin counts

**Criterion:** Valid inputs and a justified domain-specific decision criterion are required before a numerical claim; neither is manufactured here.

**Output:** No numerical output or target PASS claimed. Execution: applicability review only.

[Source definition](https://github.com/enuminous/Nightengale/blob/7a3c4a7fd4252a052384b214ac6456eb94b37eaf/nightingale.py) · [Audit evidence](PROTOCOL.md)

## 51. Zoo-Monster — FAIL

**Operation:** PASS only if every required condition meets tolerance and no failure boundary is observed

**Inputs:** Twelve frozen parser cases, identical expected-acceptance oracle, correctness tolerance 1.

**Transformation:** envelope=(min performance, mean performance, max performance) over frozen conditions; PASS only if every required condition meets tolerance and no failure boundary is observed

**Criterion:** All registered conditions must meet tolerance; any observed violation fails.

**Output:** Eight of twelve case expectations met; four invalid inputs accepted. Execution: pinned Python source executed.

[Source definition](https://github.com/enuminous/Zoo-Monster/blob/95f475ccffa30afe1853659dfd9431734b2788e0/src/monster.py) · [Audit evidence](evidence/checks.json)

## 52. Circus — FAIL

**Operation:** FAIL = material feedback OR open material risk OR bad independent check; missing provenance→N/A

**Inputs:** Broad certification claim, documented stages, explicit unresolved material semantic risk.

**Transformation:** material feedback = any dependency marked material AND feedback=true; FAIL = material feedback OR open material risk OR bad independent check; missing provenance→N/A

**Criterion:** Fixed source gate rejects open material risk; no inferred certification.

**Output:** Broad certification rejected; no refutation of the formal theorem. Execution: pinned Python source executed.

[Source definition](https://github.com/enuminous/Circus/blob/647c91dc06b4ea48871c06608298b46f00f68f99/src/circus.py) · [Audit evidence](evidence/checks.json)
