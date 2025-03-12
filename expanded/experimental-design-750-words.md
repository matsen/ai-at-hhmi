

## DASMs for antibodies 

We will first build on our successes building general antibody selection models by scaling up and modernizing our architectures.

We will also develop implicit antigen-specific models by leveraging clonal family structure.
Clonal families are collections of antibody sequences that descend from a common ancestor created by VDJ recombination.
They differ from this ancestor through the mutation and selection processes that form affinity maturation.
It is very rare that an antibody will change epitope (i.e. binding target) in the course of affinity maturation.
Thus, although we do not know what epitope is bound by a given clonal family, we can assume that all sequences in it bind the same epitope.

We can leverage this hidden epitope label for each clonal family by expanding our model to include information from the rest of the clonal family.
We are currently trialing this idea by doing limited fine-tuning for small clonal families to see if prediction is improved.
If this works, we will expand our networks to ingest information from entire clonal families at a time.

We are also excited to perform selection inference for insertion-deletion events in antibody sequences.
A simple way to do this will be to have another track of output that indicates the selective effect of insertion-deletion events. The next step after that would be to make a complete autoregressive model which would generate a child sequence probabilistically from the parent sequence. 
This has not yet been done in the mutation-selection setting.


## DASMs for viral evolution

We are building the foundation for DASMs on viral evolution.
We already have a neutral model for SARS-CoV-2, which incorporates local sequence context, RNA pairing, and genomic position effects.
We are just starting to build the same type of model for influenza.

With these ingredients, the DASM inference will proceed as for antibodies.
As before, we will infer parent-child pairs of sequences from large phylogenetic trees built on multiple sequence alignments.
We will need to infer gappy internal sequences

ArPIP algorithm linear time https://academic.oup.com/sysbio/article/72/2/307/6648472

We will perform refined pairwise codon alignment for these parent-sequence pairs, identifying and annotating insertion and deletion events.


Yun, I'm starting to wonder about the feasibility and utility of trying to infer deep natural selection models for proteins in general.
As I think you know, the idea is that by focusing on the selection component using an explicit mutation-selection model, one can more clearly get an idea of the structurally-relevant signal of evolution.
This has worked very well for antibodies, where we get a diversity of sequences but parent-child pairs are relatively close together.

It would seem exciting to extend this to proteins in general.
The advantages would be the same as for 

MSA transformer does 

Pre-training Dataset Models are trained on a dataset of
26 million MSAs. An MSA is generated for each UniRef50
(Suzek et al., 2007) sequence by searching UniClust30
(Mirdita et al., 2017) with HHblits (Steinegger et al., 2019).
The average depth of the MSAs is 1192. See Fig. A.2 for
MSA depth distribution.

Then build trees.





## DASMs for proteins in general


3. Longer term (first release in 2-3 years): Develop general-purpose protein selection models. Our formulation is not specific to viruses or the immune system but will require phylogeny and ancestral sequence reconstruction at massive scale. We will train on UniRef to create comprehensive open-source models.


