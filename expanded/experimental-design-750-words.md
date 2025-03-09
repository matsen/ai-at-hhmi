Note: I'm treating this as the methods section, even if the question seems like it's about lab experiments.

Many things will carry over from antibodies.  

PCP = parent-child pair, which is a pair of parent and child sequences in a phylogenetic tree.

Main technical challenge is handling indels in the model. Simple and complex options:

1. Allow indels in data, and make PCPs pairwise alignments, and allow gap sequences corresponding to insertion and deletion events. I think that the way to do this would be to have another track of output that indicates the selective effect of indel events. The deletion output would indicate the selective effect of a deletion at that site, and the insertion output would indicate the selective effect of an insertion directly after that site.
2. Go full autoregressive. Parent sequence in and child sequence out. I don't know exactly how this would go yet. We would need an autoregressive mutation model, and then I guess we would have the selection model sit on top of that? It's just interesting because I think of autoregressive models as being probabilistic whereas I think these selection models are really doing regression rather than probability estimation.

We will also have to do codon-based multiple sequence alignment, then trees, on lots of collections of sequences, from antibodies to uniref.
That will require some benchmarking of tools, care, and scale-up.