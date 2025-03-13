I suspect that we could handle this project entirely on our own.

That said, it would be faster and more fun to collaborate with AI@HHMI scientists as follows:

### AI Scientist (1.0 FTE)
We would benefit from dedicated personnel to explore model variants and optimize training schemes. While our current approach is performing well with a standard PyTorch transformer architecture and basic training methodology, additional research expertise would enable us to:
- Investigate and implement alternative attention mechanisms such as Flash Attention and Rotary Position Embeddings (RoFormer)
- Conduct ablation studies to identify optimal model configurations
- Design and execute comparative experiments between model variants
- Explore novel architectural modifications for our specific setting, such as fitting DASM inference as a layer in the middle of a generic protein language model

### AI Engineer (0.5 FTE)
Engineering support could improve our technical infrastructure:
- Evaluate and potentially integrate frameworks like PyTorch Lightning for streamlined training
- Implement experiment tracking solutions (e.g., Weights & Biases) for better reproducibility
- Prepare models for deployment to platforms such as Hugging Face
- Optimize model performance and efficiency for both training and inference

### Data Engineer (0.75 FTE)
Our data preparation needs are to infer phylogenetic trees and perform ancestral sequence reconstruction. Although we are performing this work on our own, additional help would allow us to:
- Build a more robust and reproducible pipeline
- Explore alternative reconstruction methods
- Implement improved computational scaling, which will be important for scaling up to UniRef
- Prepare a more elegant release of our trees and ancestral sequences, including browsing tools

These personnel would accelerate development and allow us to focus on core model development and biological interpretation.