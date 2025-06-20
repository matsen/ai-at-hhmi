# Code Evaluation Rubric for AI Scientist Position

## Code Quality (40% of total score)

### Architecture & Design (0-10 points)

**Excellent (8-10):**
- Clear separation of concerns (model, data, training, evaluation)
- Configurable components using dataclasses or config files
- Abstractions that enable reuse across different experiments
- Interfaces that allow easy extension and modification

**Good (5-7):**
- Some modularity but occasional mixing of concerns
- Most parameters are configurable
- Code can be adapted with moderate effort

**Poor (0-4):**
- Monolithic scripts with intertwined logic
- Hardcoded values throughout
- Would require significant rewrite for different use cases

### Code Reusability & Flexibility (0-10 points)

**Excellent (8-10):**
```python
# Example: Flexible experiment framework
class ExperimentRunner:
    def __init__(self, model_factory, data_loader, metrics):
        self.model_factory = model_factory
        self.data_loader = data_loader
        self.metrics = metrics
    
    def run(self, config: ExperimentConfig):
        # Fully parameterized, works with any model/data/metrics
```

**Good (5-7):**
- Functions accept parameters instead of using globals
- Some effort to make code generalizable
- Reasonable default values with override options

**Poor (0-4):**
```python
# Example: Brittle, single-purpose
def train():
    model = MySpecificModel(768, 12)  # hardcoded architecture
    train_data = load_data("./data/train.txt")  # hardcoded path
    # 200 lines of non-reusable training code
```

### Language Proficiency (0-10 points)

**Excellent (8-10):**
- Leverages Python features appropriately (generators, context managers, decorators)
- Uses vectorized operations instead of loops where appropriate
- Proper use of standard library and common ML libraries
- Type hints used consistently and correctly

**Good (5-7):**
- Generally good Python usage with occasional missed opportunities
- Some type hints
- Mostly follows Python conventions

**Poor (0-4):**
- Writes C-style Python (explicit loops, manual memory management patterns)
- No type hints
- Misses obvious Pythonic solutions

### DRY Principles & Abstraction (0-10 points)

**Excellent (8-10):**
```python
# Example: Proper abstraction
class AttentionBase(ABC):
    @abstractmethod
    def forward(self, q, k, v, mask=None):
        pass

class MultiHeadAttention(AttentionBase):
    # Reusable implementation

class FlashAttention(AttentionBase):
    # Alternative implementation with same interface
```

**Good (5-7):**
- Identifies common patterns and extracts functions
- Minimal code duplication
- Some shared utilities

**Poor (0-4):**
- Copy-pasted code blocks with minor variations
- No attempt to identify common patterns
- Repeated implementations of the same logic

## Technical Skills (50% of total score)

### ML Fundamentals Understanding (0-15 points)

**Excellent (12-15):**
- Can explain attention mechanism mathematically and computationally
- Understands O(n²) complexity and memory implications
- Knows optimization techniques (gradient accumulation, mixed precision)
- Can reason about model behavior and debugging strategies

**Good (8-11):**
- Solid understanding of transformers and training dynamics
- Some awareness of computational constraints
- Can implement standard architectures correctly

**Poor (0-7):**
- Surface-level understanding only
- Cannot explain why certain design choices were made
- Struggles with debugging or optimization questions

### Engineering Practices (0-15 points)

**Excellent (12-15):**
- Comprehensive logging and monitoring
- Proper error handling and recovery
- Reproducible experiments with seed management
- Performance profiling and optimization
- Clear documentation and docstrings

**Good (8-11):**
- Basic logging and error handling
- Some attention to reproducibility
- Reasonable documentation

**Poor (0-7):**
- Print debugging only
- No error handling
- Cannot reproduce results
- Minimal or no documentation

### Experimental Design (0-10 points)

**Excellent (8-10):**
- Systematic approach to hyperparameter tuning
- Proper validation methodology
- Clear metrics and evaluation criteria
- Thoughtful ablation studies

**Good (5-7):**
- Standard train/val/test splits
- Some hyperparameter exploration
- Basic metrics tracking

**Poor (0-4):**
- Ad-hoc experimentation
- No clear evaluation strategy
- Results not properly validated

### Modern Tools & Practices (0-10 points)

**Excellent (8-10):**
- Uses experiment tracking (W&B, TensorBoard, etc.)
- Leverages AI coding assistants effectively
- Familiar with modern efficiency techniques
- Good git practices and version control

**Good (5-7):**
- Some use of modern tools
- Basic version control
- Open to learning new techniques

**Poor (0-4):**
- No experiment tracking
- Unfamiliar with modern tools
- Poor or no version control

## Research Impact (10% of total score)

### Publication Quality (0-5 points)
- Impact and relevance of publications
- Technical depth of contributions
- Clarity of writing and presentation

### Open Science Practices (0-5 points)
- Effort to make research reproducible
- Community engagement
- Documentation quality

## Scoring Summary

Total possible: 100 points

- **Exceptional (90-100):** Top 5% - Immediate interview
- **Strong (75-89):** Top 20% - Likely interview  
- **Solid (60-74):** Top 40% - Consider based on other factors
- **Below Bar (<60):** Not ready for this role

## Red Flag Overrides

Automatic disqualification if:
- Code contains obvious security vulnerabilities
- Evidence of plagiarism or misrepresentation
- Cannot explain their own code
- No evidence of actual implementation experience