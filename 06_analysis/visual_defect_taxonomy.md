# Visual Defect Taxonomy

| Defect | Description | Possible cause | Fix direction |
|---|---|---|---|
| plastic_skin | Skin looks waxy, airbrushed, or lacks tonal variation. | Too much smoothing or high beauty strength. | Reduce strength, add natural variation, inspect crops. |
| glassy_eyes | Eyes look wet, glassy, or artificial. | Prompt, enhancer, or video model changes eyes too strongly. | Preserve eyes and reduce eye transformation. |
| rubber_lips | Lips lose texture or natural edge. | Over-enhancement or bad animation. | Reduce mouth and lip manipulation. |
| beard_artifacts | Beard looks painted or flickers. | Weak base avatar or video model instability. | Improve still, refine crop, reduce motion. |
| identity_drift | Face changes across passes. | Too much regeneration. | Lower transformation strength and use selected stills. |
| overbeautified | Result looks like a generic AI influencer. | Prompt or style too generic. | Use a more specific character brief. |
| ashy_skin | Dark or warm skin becomes gray or washed out. | Wrong color correction or over-lighting. | Use tone-safe correction. |
| video_face_slip | Face slides or morphs in video. | Weak still or overly strong motion. | Improve still and reduce motion prompt. |
