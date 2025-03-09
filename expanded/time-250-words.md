## Antibody models

* We already have completed deep natural selection models, a predecessor of the Deep Amino acid Selection Models (DASMs) proposed here, which got positive peer review.
* By mid-June we will post and release our first DASM models for antibodies.
* We will continue to scale, refine, interpret, and develop software to fine-tune these models for antigen targets in the coming years.

## Virus evolution models

We think that influenza will be the best first virus for which to develop a DASM, as it has a nice balance of evolutionary diversity and many sequences.

1. We are just beginning to fit a mutation model for influenza, which will be ready in 4 months or less, given that it follows the same path as our prior work on SARS-CoV-2.
2. Simultaneously, we will generalize our current code 

2. Medium term (first release in 1 year): Apply our framework to systems with closely related sequences, such as influenza and SARS-CoV-2. We already have a neutral model for SARS-CoV-2 and expect the resulting fitness predictions to provide higher resolution than existing models. We are starting this work now.

3. Longer term (first release in 2-3 years): Develop general-purpose protein selection models. Our formulation is not specific to viruses or the immune system but will require phylogeny and ancestral sequence reconstruction at massive scale. We will train on UniRef to create comprehensive open-source models.

