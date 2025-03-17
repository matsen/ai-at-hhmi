# Inviting Darwin into protein foundation models

## Overall Vision and Goals

Our project will integrate evolutionary biology principles into protein language models.  Specifically, we will train models of natural selection for antibodies, viruses, and proteins more generally.

Evolution is fundamentally a process of mutation and selection, yet current protein language models ignore this biological reality.  Current models are trained using masked loss on observed sequences, which removes proteins from their phylogenetic context and ignores the nucleotide-level processes driving evolution.

## Success with Antibodies

Our work with antibodies demonstrates the importance of this approach.  We've shown that antibody language models like AbLang2 estimate amino acids coded by codon neighbors as being two orders more likely than non-neighbors, and show clear effects of neutral mutation probability (Figures 4A and 4B).  These factors negatively impact functional prediction (Figure 4C).  Because current models must implicitly learn mutation-level processes, they will always be deficient because they do not have access to nucleotide sequence.

We have developed a Deep Amino acid Selection Model (DASM) that leverages a separately-fit mutation model (Figure 1).  Specifically, we model the probability of a given codon c at a given site j after evolutionary time t as the product of a mutation term p(j, c, t) and a selection term f(j, c) which has access to the entire protein sequence.

For antibodies, mutation is modeled by a convolutional neural network and selection by a modest-sized transformer-encoder.  Rather than using masked-modeling objectives, our model predicts the location and identity of mutations in antibody evolution.

This approach performs better on all metrics: improved out-of-sample prediction (Figure 3), superior performance on functional benchmark tasks (Table 1), and greater interpretability.  DASM is an order of magnitude smaller than modern antibody language models, trained on far less data, and two orders of magnitude faster to run.

## Extending to Viruses and All Proteins

We will follow a three-phase approach:

1. Short term (first release in months): Scale up antibody models with larger datasets and develop antigen-specific models using clonal family structure and antigen-specific data.

2. Medium term (first release in 1-2 years): Apply our framework to viral sequences, such as influenza and SARS-CoV-2.  This will expand the state of the art by giving predictions of maximum resolution yet being able to leverage information from many sequence alignments (Figure 2), such as for influenza H1 and H3.  We already have a neutral model for SARS-CoV-2 and expect the resulting fitness predictions to provide higher resolution than existing models.  We are starting this work now.

3. Longer term (first release in 2-3 years): Develop general-purpose protein selection models.  Our formulation is not specific to viruses or the immune system but to train a general model will require phylogeny and ancestral sequence reconstruction at a large scale.  We will train on UniRef to create comprehensive open-source models.

## Deliverables

Our open-source models will accurately capture the functional aspects of protein evolution across domains.  They will be more accurate, smaller, faster, and more interpretable than current approaches, bringing biology back into the center of biological foundation models.

We take software seriously and will deliver convenient and accurate open-source models for the community.

We will also deliver pre-computed results and visualization tools.  Thus far we have built a prototype https://matsengrp.github.io/dnsm-viz/ built on Bloom lab `dms-viz` software.
