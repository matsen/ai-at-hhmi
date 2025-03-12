## DASMs for viral evolution

DASMs will generalize and unify methods that have brought insight in the analysis of viral sequences. 
For example, Jesse Bloom's `phydms` software can reveal the effects of natural selection above and beyond the selection observed in a lab deep mutational scan (DMS).
However, it can work with at most 100 sequences at a time and depends on having an actual DMS experiment available.
It also requires a minimum number of sequences to have sufficient power, which can be limiting in outbreak settings.

> I don't see how the following fits in.
The Bloom-Neher viral fitness estimation framework has provided valuable insight into the evolution of viral fitness through time.
However, it requires the huge volume of sequencing available mid-pandemic, and the current level of sequencing is likely to be insufficient.

A DASM would scale to even the largest viral datasets and yet work in a low-data regime by drawing strength between more distantly related sequences.
It would also provide a flexible framework in which one could input additional covariates and data.
This could include calendar time, which would be a proxy for immune exposures.
It could also include a recently-developed high-throughput neutralization assay developed by the Bloom lab.

### Definitely OK

Trevor Bedford is currently working on integrating protein sequence features into his predictive frameworks. 
We expect that a DASM would provide more relevant protein features than existing work.

We could fit a DASM using the sequence data and then compare it to a DMS at a given sequence and use that to infer immune selection.

We could also include calendar time.

We could also include DMS into the loss function.

What would it look like to include the neutralization data?
It's not parent-child pairs.


