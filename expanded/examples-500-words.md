## DASMs for antibodies

I have already seen how DASMs provide much better prediction of functional properties in the zero-shot (i.e. no labeled training data) setting.
Furthermore, our training data has no antigen labels, so the fact that the model can predict binding at all is a welcome surprise.

We expect that fine-tuning on data that is enriched in antigen-specific data will reveal the landscape of binders.
We also believe that building a model that takes an entire clonal family's worth of data (see Experimental Design) will enable implicit antigen-specific prediction: even though we don't know the epitope, we know that all sequences in a given clonal family will bind that epitope.
We also expect that the protein embeddings for DASMs, given that they are free from the confounding effects of SHM, will be more predictive of functional properties than their classical counterparts.

## DASMs for viral evolution

Evolutionary analysis of viral sequences has led to many insights about how viruses adapt to immune pressures, however, conclusions are necessarily limited in precision because the statements made by the evolutionary models are on the level of sequence alignments.
When doing an analysis for a given virus, one collects sequence for that virus and can make statements about how selection acts on that collection of sequences.
If one has a lot of data, one can make a statement about the selection acting per-site for that virus, however, due to model limitations, one cannot learn per-sequence per-site using existing methods (Figure~3, top).

DASMs, in contrast, do return per-sequence per-site estimates of natural selection (Figure~3, bottom).
In fact, we infer per-sequence per-site per-amino-acid estimates, and have shown using functional assays and investigations that these estimates are meaningful.
This is enabled by training on lots of related datasets, only one of which may contain a virus of interest.

As an example, imagine we are interested on comparing the selection pressure on a single H5N1 sequence in humans. 
In the classical setting, one would gather a collection of H5N1 hemagglutinin sequences, of which there aren't very many, and perform an evolutionary analysis for that alignment.
This analysis would lack power.
One might want to add other sequences, such as H1N1 sequences, but that would distort the inference.

In the DASM case, one could train a model using not only all hemagglutinin sequences from influenza, but also all of the hemagglutinin from the Orthomyxoviridae and Paramyxoviridae.
In fact, one could probably benefit by considering all proteins as described in the next section.

The predictions will be readily interpretable.
Jesse Bloom's `phydms` software can reveal the effects of natural selection above and beyond the selection observed in a lab deep mutational scan (DMS).
However, it requires an entire sequence alignment, and predicts a per-site selection estimate.
With a DASM, one can directly compare the output to the DMS, simply reading off the differences.

It would also provide a flexible framework in which one could input additional covariates and data.
This could include calendar time, which would be a proxy for immune exposures.
It could also include a recently-developed high-throughput neutralization assay developed by the Bloom lab.
It could even include a measure of the number of descendants of a sequence, as in the Bloom-Neher viral fitness estimation framework which has provided valuable insight into the evolution of viral fitness through time.


## DASMs for proteins in general

I expect DASMs to do everything that the ESM2 model could do, except more accurately and faster.