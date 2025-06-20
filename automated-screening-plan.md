# Automated Screening Plan for 1000 AI Scientist Applications

## System Architecture

### Directory Structure
```
applications/
├── candidate_001/
│   ├── cv.pdf
│   ├── cover_letter.pdf
│   ├── code_sample.py (or .zip)
│   ├── publications/
│   └── metadata.json
├── candidate_002/
└── ...
```

### Output Structure
```
screening_results/
├── candidate_profiles/       # Individual JSON profiles
├── rankings.csv             # Sorted candidate list
├── evaluation_logs/         # Detailed scoring logs
└── shortlist_report.md      # Top candidates summary
```

## Phase 1: Data Extraction & Parsing

### 1.1 Document Parsing
```python
# Pseudo-code for extraction pipeline
for candidate_dir in applications/:
    - Extract text from CV (PDF → text)
    - Parse cover letter
    - Identify GitHub links, personal websites
    - Extract publication list
    - Create initial candidate profile JSON
```

### 1.2 Code Discovery
- Scan submitted code samples
- Extract GitHub URLs from CV/cover letter
- Search for code links in publications
- Clone repositories locally for analysis

## Phase 2: Automated Code Analysis

### 2.1 Static Analysis Pipeline
```python
def analyze_code_quality(code_path):
    metrics = {
        'file_structure': analyze_architecture(code_path),
        'abstraction_score': measure_abstractions(code_path),
        'duplication_score': detect_code_duplication(code_path),
        'flexibility_score': assess_configurability(code_path),
        'python_proficiency': check_pythonic_patterns(code_path)
    }
    return metrics
```

### 2.2 Specific Checks

**Architecture Analysis:**
- Count hardcoded values vs configuration
- Measure coupling between modules
- Identify abstraction patterns
- Check for separation of concerns

**DRY Violation Detection:**
- Use AST analysis to find similar code blocks
- Identify copy-paste patterns
- Measure function/class reuse
- Flag repeated implementations

**Python Proficiency:**
- Check for list comprehensions vs loops
- Identify use of standard library features
- Look for type hints
- Assess use of Python idioms

### 2.3 Git History Analysis (if available)
- Commit message quality
- Code evolution over time
- Collaboration patterns
- Documentation updates

## Phase 3: Technical Assessment

### 3.1 CV/Cover Letter Analysis
```python
technical_keywords = {
    'essential': ['attention', 'transformer', 'pytorch', 'deep learning'],
    'advanced': ['flash attention', 'computational complexity', 'optimization'],
    'bonus': ['state space models', 'efficient transformers', 'kernel methods']
}

def score_technical_knowledge(text):
    # NLP analysis for technical depth
    # Look for not just keywords but context
    # "implemented attention" > "familiar with attention"
```

### 3.2 Publication Analysis
- Parse publication titles/abstracts
- Identify ML/DL papers
- Check implementation claims
- Score technical relevance

## Phase 4: Scoring & Ranking

### 4.1 Composite Scoring
```python
def calculate_final_score(candidate):
    weights = {
        'code_quality': 0.40,
        'technical_skills': 0.50,
        'research_impact': 0.10
    }
    
    # Sub-scores from rubric
    code_score = (
        candidate['architecture'] * 0.25 +
        candidate['reusability'] * 0.25 +
        candidate['language_proficiency'] * 0.25 +
        candidate['dry_principles'] * 0.25
    )
    
    technical_score = (
        candidate['ml_fundamentals'] * 0.30 +
        candidate['engineering_practices'] * 0.30 +
        candidate['experimental_design'] * 0.20 +
        candidate['modern_tools'] * 0.20
    )
    
    return weighted_sum(scores, weights)
```

### 4.2 Ranking Strategy
1. Apply minimum thresholds (must have Python, ML experience)
2. Score all candidates
3. Identify natural clusters in scores
4. Flag anomalies for human review
5. Generate tiered rankings

## Phase 5: Report Generation

### 5.1 Individual Reports
For top 50 candidates, generate:
- Executive summary with strengths/weaknesses
- Code quality examples (good and bad)
- Technical depth indicators
- Specific concerns or highlights

### 5.2 Batch Analytics
- Score distributions
- Common weaknesses in candidate pool
- Correlation analysis (code quality vs publications)
- Diversity metrics

## Implementation Tools

### Core Technologies
- **Claude Code + MCP**: Orchestration and file handling
- **Python AST**: Code analysis
- **Tree-sitter**: Multi-language parsing
- **Pandas**: Data management and ranking
- **PyPDF2/pdfplumber**: PDF extraction

### Parallel Processing
```python
# Process candidates in batches
from concurrent.futures import ProcessPoolExecutor

def process_batch(candidate_ids):
    with ProcessPoolExecutor(max_workers=8) as executor:
        results = executor.map(analyze_candidate, candidate_ids)
    return results
```

## Quality Control

### Validation Steps
1. Manually review 5% sample to calibrate scoring
2. Check edge cases (very high/low scores)
3. Ensure no good candidates filtered by automation
4. Compare automated scores with human judgment

### Human-in-the-Loop
- Flag candidates with conflicting signals
- Review borderline cases (scores near cutoffs)
- Manually inspect top 10% code samples
- Verify no false negatives in bottom 50%

## Execution Timeline

1. **Setup (Day 1)**: Configure environment, test on 10 candidates
2. **Batch Processing (Days 2-3)**: Run automated analysis
3. **Review & Calibration (Day 4)**: Adjust scoring based on samples
4. **Final Ranking (Day 5)**: Generate reports and shortlist
5. **Human Review (Days 6-7)**: Deep dive on top candidates