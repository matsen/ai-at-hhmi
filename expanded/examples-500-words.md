## DASMs for antibodies

We have already shown how DASMs provide much better prediction of functional properties in the zero-shot (i.e. no labeled training data) setting (Table 1).  With our training data having no antigen labels, the model's ability to predict binding is a welcome surprise.

As a next step, fine-tuning on antigen-specific data will reveal the landscape of binders in greater resolution.  However, antigen-labeled data is limited, thus we will use the fact that all sequences in a given clonal family (i.e. the descendants of a given naive antibody sequence) will bind a single epitope.  Thus, we will build a model that takes an entire clonal family's data to enable implicit antigen-specific prediction.

These antigen-specific models will predict binding affinities more accurately, leading to better antibody design.

Also, the protein embeddings for DASMs, free from the confounding effects of mutation, will be more predictive of functional properties when using them for regression.


## DASMs for viral evolution

Evolutionary analysis of viral sequences has led to insights about viral adaptation, but conclusions are limited because evolutionary models give overall inferences for entire sequence alignments.  For a given virus, one can make per-site selection statements with sufficient data, but cannot learn per-sequence per-site using existing methods (Figure 4, top).  In other words, existing methods do not account for epistasis.

In contrast, DASMs return per-sequence per-site estimates of natural selection (Figure 4, bottom).  In fact, we infer per-sequence per-site per-amino-acid estimates, validated through functional assays.  This is enabled by training on many related datasets, which in the antibody case are different clonal families.

A similar concept applies for viruses.  For example, when studying selection pressure on an H5N1 sequence in humans, traditional analysis would align H5N1 hemagglutinin sequences and perform evolutionary analysis, lacking power because these sequences are few.  Adding other sequences, such as from H1N1, would distort the inference.

With DASMs, one could train using all viral hemagglutinin sequences, and even go beyond to lectins in general.  Then one could ask for an inference for a given H5N1 sequence, leveraging all the data but making a precise prediction.

The predictions will answer questions of interest for evolutionary virologists.  While Bloom's `phydms` software reveals natural selection effects beyond lab deep mutational scans (DMS), it requires a sequence alignment and predicts overall per-site selection for that entire sequence alignment.  In contrast, one can directly compare the per-site per-amino acid output of a DASM to the DMS, by simply reading off the differences.

We also note that the DASM framework can easily account for complex mutational processes, like we uncovered with SARS-CoV-2.  These can confound `phydms` and classical dN/dS approaches.

The deep-learning paradigm also provides a framework to input additional covariates like calendar time, high-throughput neutralization assays, or measures of the success of descendant sequences.


## DASMs for proteins in general

The ESM class of models pioneered protein language modeling and remains the most widely used approach today.  Trained on the entire UniRef database using masked language modeling, ESM has demonstrated remarkable versatility across tasks from variant effect prediction to structure determination.  This success has made it the foundation for EvolutionaryScale, a startup that recently secured $142M in venture capital funding to develop closed-source protein language models.

Because these tasks concern protein sequence function, and not mutation, I expect DASMs to perform better than such a model trained using masked language modeling.
