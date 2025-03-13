We already have DASMs working for antibodies, showing superior characteristics on all fronts: they fit better, predict functional properties better, and are smaller and faster (Table 1). 

Thus we have a clear proof of concept for a real use case.

For extending to other classes of proteins, the primary modification will be from a setting with perfect sitewise homology with no indel events, to one where meaningful and important insertion and deletion events happen.
We will be able to extend our current set of models to handle this setting by simply masking sites with insertions and deletions.
Although we have some ideas about how to treat insertions and deletions as meaningful events, there is some risk that we won't be able to meaningfully extend the model to handle them.
However, I think this is an "optional extra".

For viral datasets, we don't know if the smaller scale of data will result in a too-flexible model that will overfit, and if extending training to many related proteins will reduce overfitting.
However, we should know within 6 months of properly training models whether or not this is going to work.

The final phase of the project will require homology clustering, multiple sequence alignment, and phylogeny on all known proteins. This is a major computational task, but tools exist spanning the range of accuracy vs computational efficiency.

Other risks:

1. There is AI risk. ESM3, for example, has guardrails to prevent malicious acts and is not publicly available. If things go as planned then this will be a more useful model than ESM. We are specifically interested in viral proteins.
2. There is a risk that EvolutionaryScale will patent DASMs if they heard about the project through our one-step connections.