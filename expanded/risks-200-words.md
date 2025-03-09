We already have DASMs working for antibodies, showing superior characteristics on all fronts: they fit better, predict functional properties better, and are smaller and faster. 

Thus we have a clear proof of concept for a real use case.

For extending to other classes of proteins, the primary modification will be from a setting with perfect sitewise homology with no indel events, to one where meaningful and important insertion and deletion events happen.

There is some risk that we won't be able to meaningfully extend the model to handle indels. However, in the worst case, we can simply ignore these events and indeed this will be our first version. We also have reasonable ideas about how to extend the models, and will be starting work on those soon.

The project will also be required to do homology clustering, multiple sequence alignment, and phylogeny on the known collection of proteins. It seems possible that this would be a blocker, though there are many different algorithms that balance accuracy and runtime and I would be surprised if we couldn't find something appropriate.

Other risks:

1. There is a risk that EvolutionaryScale will beat us to the punch and patent. But our existing work seems like clear prior art, and we can mention that one could do this for proteins in general.
2. There is also AI risk. ESM3, for example, has guardrails to reduce malicious acts and is not publicly available. If things go as planned then this will be a more useful model than ESM.