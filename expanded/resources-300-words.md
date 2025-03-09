So far we are doing fine with 2 A100 GPUs and 10 or so L40S GPUs. 
I expect that to work for the antibody and viral datasets.

For scaling up to training general models like ESM:

ESM models were trained over 512 NVIDIA V100 GPUs for about a month or two: "We trained each model over 512 NVIDIA V100 GPUs. ESM2 700M took 8 days to train. The 3B parameter LM took 30 days. The 15B model took 60 days. All language models were trained for 500K updates, except the 15B language model which we stopped after 270K updates due to computational constraints."

That was a few generations of GPU ago.

A100 is roughly 2-3× faster than V100 for training large language models
H100 is roughly 3-4× faster than V100 for training large language models


For clustering sequences into homologous groups, then doing alignments and trees on UniRef, we will require a bunch of CPU compute.
TODO: estimate time required.
