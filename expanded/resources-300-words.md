## Antibody and viral models

So far we are doing fine with 2 A100 GPUs and about 10 L40S GPUs that we either own or share with other faculty members.  This is acceptable for our current pace of model development and model size.

If we add additional staff, such as AI Scientists, I think it would be nice for each additional FTE to have 8 to 12 GPUs available when they are in a model-training cycle.  Our current models fit on L40S GPUs, and in fact are faster to train on L40Ss than on the A100s.


## General protein models

For scaling up to training general models like ESM on UniRef, we can refer to their description of training ESM2: "We trained each model over 512 NVIDIA V100 GPUs.  ESM2 700M took 8 days to train.  The 3B parameter LM took 30 days.  The 15B model took 60 days.  All language models were trained for 500K updates, except the 15B language model which we stopped after 270K updates due to computational constraints." 

If we estimate that current GPUs are about 3x faster than V100s, then we'd need around 5,000 GPU-days to train an ESM2 equivalent.

The major bottleneck for this project may be the CPU compute.  Inferring alignments and trees on millions of alignments naively using the most accurate methods could easily take thousands of CPU-years to complete.  Thus we will need to find a balance between accuracy and speed, as well as potentially prioritize alignments based on structural relevance and novelty.
