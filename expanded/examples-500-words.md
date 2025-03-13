## DASMs for antibodies

I have already seen how DASMs provide much better prediction of functional properties in the zero-shot (i.e. no labeled training data) setting.
With our training data having no antigen labels, the model's ability to predict binding is a welcome surprise.

As a next step, fine-tuning on antigen-specific data will reveal the landscape of binders.
However, antigen-labeled data is limited, thus we will use the fact that all sequences in a given clonal family (i.e. the descendants of a given naive antibody sequence) will bind a single epitope.
Thus, we will build a model that takes an entire clonal family's data to enable implicit antigen-specific prediction.
The protein embeddings for DASMs, free from SHM confounding effects, will be more predictive of functional properties.

## DASMs for viral evolution

Evolutionary analysis of viral sequences has led to insights about viral adaptation, but conclusions are limited because evolutionary models give overall inferences for entire sequence alignments.
For a given virus, one can make per-site selection statements with sufficient data, but cannot learn per-sequence per-site using existing methods (Figure~3, top).

In contrast, DASMs return per-sequence per-site estimates of natural selection (Figure~3, bottom).
In fact, we infer per-sequence per-site per-amino-acid estimates, validated through functional assays.
This is enabled by training on related datasets, which in the antibody case are different clonal families.

A similar concept applies for viruses.
For example, when studying selection pressure on an H5N1 sequence in humans, traditional analysis would gather H5N1 hemagglutinin sequences and perform evolutionary analysis, lacking power because these sequences are few.
Adding other sequences, such as from H1N1, would distort the inference.

With DASMs, one could train using hemagglutinin sequences from influenza, Orthomyxoviridae and Paramyxoviridae, or even all proteins.
Then one could ask for an inference for a given H5N1 sequence, leveraging all of the data but making a precise prediction.

The predictions will answer questions of interest for evolutionary virologists.
While Bloom's `phydms` software reveals natural selection effects beyond lab deep mutational scans (DMS), it requires a sequence alignment and predicts overall per-site selection for that entire sequence alignment.
In contrast, one can directly compare the per-site per-amino acid output of a DASM to the DMS, by simply reading off the differences.

The deep-learning paradigm also provides a framework to input additional covariates like calendar time, high-throughput neutralization assays, or measures of the success of descendant sequences.

## DASMs for proteins in general

The ESM class of models was the first and still most used protein language models.
It is trained using masked language modeling on all of UniRef.
It has shown its versatility in tasks from predicting variant effects to (forming the basis of) structure prediction.
It is the foundation for a startup, EvolutionaryScale, which recently got $142M in VC funding, and produces closed-source models.

Because these tasks concern protein sequence function, and not mutation, I expect DASMs to perform better than such a model trained using masked language modeling.