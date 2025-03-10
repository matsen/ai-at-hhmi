## Antibody models (first release in months)

* We already have completed deep natural selection models, a predecessor of the Deep Amino acid Selection Models (DASMs) proposed here, which got positive peer review.
* By mid-June we will post and release our first DASM models for antibodies.
* We will continue to scale, refine, interpret, and develop software to fine-tune these models for antigen targets in the coming years.

## Virus evolution models (first release in 1-2 years)

We think that influenza will be the best first virus for which to develop a non-antibody DASM, as it has a nice balance of evolutionary diversity and many sequences.

1. We are just beginning to fit a mutation model for influenza, which will be ready in 4 months or less, given that it follows the same path as our prior work on SARS-CoV-2.
2. Starting this summer, we will generalize our current code to work with indels.

## General selection models for proteins (first release in 2-3 years)

Once we have experience with viruses, we can turn our attention to proteins in general.

We will need to cluster all of UniRef into homologous groups, build alignments, build trees, and perform ancestral sequence reconstruction. Along the way, we will need to find a good balance between accuracy and runtime.

After that the same conceptual framework will apply as for other proteins, but we will need to do major scale-up and will want to experiment with architectures.