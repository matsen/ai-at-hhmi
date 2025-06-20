# AI Scientist Screening Criteria

## Technical Knowledge Assessment

### Modern AI Architecture Knowledge
- [ ] Can explain attention mechanism in detail (query, key, value operations)
- [ ] Understands the O(n²) computational complexity of standard attention
- [ ] Aware of memory bottlenecks in attention computation
- [ ] Knows about Flash Attention or similar efficiency improvements (bonus)
- [ ] Familiar with alternative architectures like state space models (bonus)

### AI Development Tools
- [ ] Knows what Model Context Protocol (MCP) is and its applications
- [ ] Has experience with AI coding assistants (GitHub Copilot, Cursor, Claude, etc.)
- [ ] Can articulate how they use AI tools to accelerate their research workflow
- [ ] Understands the limitations and best practices for AI-assisted development

### ML Engineering Fundamentals
- [ ] Can explain their approach to experiment tracking and reproducibility
- [ ] Understands GPU memory optimization strategies
- [ ] Familiar gradient accumulation
- [ ] Can discuss profiling and debugging strategies for deep learning code

## Code Quality Assessment

### Code Sample Requirements
Request: "Please submit a code sample (500-1000 lines) from a recent ML research project"

Evaluate for:
- [ ] **DRY Principles**: No unnecessary code duplication, proper abstraction
- [ ] **Organization**: Clear module structure, logical separation of concerns
- [ ] **Documentation**: Meaningful docstrings, clear variable names, helpful comments
- [ ] **Configuration**: Uses config files or dataclasses instead of hardcoded values
- [ ] **Error Handling**: Graceful handling of edge cases and failures
- [ ] **Testing**: Includes unit tests or validation code

### Specific Code Quality Markers
- [ ] Uses type hints consistently
- [ ] Implements proper logging instead of print statements
- [ ] Separates model definition, training logic, and data processing
- [ ] Shows awareness of computational efficiency (vectorization, batching)
- [ ] Demonstrates clean git history and meaningful commit messages

## Research Practice Assessment

### Open Science Commitment
- [ ] **Code Availability**: If they have published papers, is the code publicly available?
- [ ] **Documentation Quality**: Are repositories well-documented with clear READMEs?
- [ ] **Reproducibility**: Do they provide scripts/configs to reproduce results?
- [ ] **Community Engagement**: Do they respond to issues or incorporate feedback?

### Research Code Examples
Ask for links to:
- [ ] GitHub profile or similar
- [ ] Code repositories from published papers
- [ ] Open source contributions
- [ ] Research notebooks or demos

## Interview Questions

### Technical Deep Dive
1. "Can you explain how attention works in transformers? Walk me through the computation"
2. "What is the computational complexity of attention and why does it matter for long sequences?"
3. "Have you heard of Flash Attention? If so, what problem does it solve?"
4. "How do you approach debugging a model that trains but doesn't converge?"
5. "Describe your workflow for running and tracking ML experiments"

### Code Quality Discussion
1. "Show us a piece of code you're particularly proud of and explain your design decisions"
2. "How do you balance research velocity with code maintainability?"
3. "Walk through how you would refactor messy research code for public release"
4. "What's your approach to testing ML code?"

### AI Tools Usage
1. "How do you use AI coding assistants in your daily workflow?"
2. "What tasks do you find AI tools most/least helpful for?"
3. "How do you verify and validate AI-generated code?"
4. "Have you built any custom tools or workflows around AI assistants?"

## Red Flags
- [ ] Cannot explain basic attention mechanism or its complexity
- [ ] No publicly available code despite multiple publications
- [ ] Code samples show poor organization or copy-pasta
- [ ] No experience with version control or collaborative development
- [ ] Dismissive of AI tools or overly reliant without understanding

## Green Flags
- [ ] Clean, well-documented GitHub profile with active contributions
- [ ] Can explain complex concepts clearly with examples
- [ ] Shows iterative improvement in code quality over time
- [ ] Balances theoretical knowledge with practical implementation skills
- [ ] Demonstrates curiosity about new techniques and tools