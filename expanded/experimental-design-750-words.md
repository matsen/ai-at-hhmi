DASMs (Deep Amino acid Selection Models) separate nucleotide mutation from protein selection in evolution, allowing us to better model evolutionary processes.  DASMs are trained using a precomputed mutation model (green box, Figure 2a), fitting the DASM selection model (purple box) with the objective of predicting the child sequence in parent-child sequence pairs in phylogenetic trees.


## Improving DASMs for antibodies 

We will first build on our successes building antibody selection models by scaling up and modernizing our architectures.

We will also develop _implicit_ antigen-specific models by leveraging clonal family structure.  Clonal families are collections of antibody sequences that descend from a common ancestor created by VDJ recombination.  Sequences differ from this ancestor through the mutation and selection processes that form affinity maturation.  It is very rare that an antibody will change binding target in the course of affinity maturation.  Thus, although we do not know what antigen is bound by a given clonal family, we can assume that all sequences in it bind the same antigen.

We can leverage this hidden antigen label for each clonal family by expanding our model to include information from the rest of the clonal family.  We are currently trialing this idea by doing limited fine-tuning for small clonal families to see if prediction is improved.

We are also excited to perform selection inference for insertion-deletion events in antibody sequences.  A simple way to do this will be to have another track of output that indicates the selective effect of insertion-deletion events.  The next step after that would be to make a complete autoregressive model which would generate a child sequence probabilistically from the parent sequence.  This has not yet been done in the mutation-selection setting.


## DASMs for viral evolution

Our next step is to use DASMs to understand viral evolution. We already have a neutral model for SARS-CoV-2, which incorporates local sequence context, RNA pairing, and genomic position effects.  We are now building the same type of model for influenza.

With these ingredients, the DASM inference will proceed as for antibodies.  In contrast to the case of antibodies, we will not be able to ignore insertions and deletions in evolution.  We will infer gappy internal sequences using either gap coding or the recently-developed linear-time ArPIP algorithm.

We will begin by inferring a DASM on just H3N2 sequences, and then progressively add other subtypes and viral families.  At every stage we will evaluate the accuracy of the prediction by comparing them to baselines using held-out data.  Baseline models will include typical mutation models used in phylogenetics, Goldman-Yang models, ESM, and also Jesse Bloom's ExpCM models that include data from deep mutational scanning (DMS) experiments that test protein function after applying every possible amino acid mutation.

We will also experiment with using conditional model fitting incorporating DMS data.  That is, we will use a loss that incorporates a DMS prediction task, however the sequence used for prediction will be labeled with a token that indicates that we are predicting DMS and not natural evolution.  This is important because natural evolution reflects many selection pressures that are not present for a lab DMS experiment.

We are also interested to understand if the DASM predicts shifts between homologs as measured by DMS.


## DASMs for proteins in general

If it proves useful to add related sequence alignments to our model training for viral proteins, we will take this work to its logical conclusion and develop a single model for all proteins.

This is not conceptually difficult.  The MSA transformer was trained on 26 million multiple sequence alignments (MSAs) generated by searching UniClust30 with HHblits for each UniRef50 sequence.  We could do something similar, or we could leverage the recent structural clustering of the AlphaFold Protein Structure Database.

We will then perform codon multiple sequence alignment, and then ancestral sequence reconstruction as described above.  The ancestral sequences will be more uncertain than in the case of antibodies or viral proteins, and we will experiment with different ways to represent this uncertainty.  

We will provide proof of concept by prioritizing alignments to add as training data to this single model based on structural relevance and novelty.  Starting with our viral datasets, we will gradually expand to include additional sequences.  First, we'll focus on FoldSeek clusters containing relevant viral proteins, then move to other clusters that are closely related according to structural similarity metrics such as TM-score and local distance difference test.  We hypothesize that including these related structures will improve performance according to our metrics.  We will track performance improvements as we incorporate additional MSAs.