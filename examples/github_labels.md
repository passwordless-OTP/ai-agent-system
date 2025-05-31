# GitHub Labels for AI Agent System

Recommended labels to add to your repository for optimal AI agent performance.

## Priority Labels

```bash
# High priority - work on first
gh label create "high priority" --color "B60205" --description "Work on this first"

# Medium priority - standard priority
gh label create "medium priority" --color "FBCA04" --description "Standard priority"

# Low priority - lower priority
gh label create "low priority" --color "0E8A16" --description "Lower priority"
```

## AI Readiness Labels

```bash
# Explicitly marked for AI processing
gh label create "ai-agent-ready" --color "0E8A16" --description "Ready for AI agent processing"

# Good entry points for AI
gh label create "good first issue" --color "7057FF" --description "Good for newcomers and AI agents"

# Community assistance welcome  
gh label create "help wanted" --color "008672" --description "Extra attention is needed"
```

## Complexity Estimation

```bash
# Simple changes (1-2 hours)
gh label create "complexity-low" --color "D4EDDA" --description "Simple changes, 1-2 hours estimated"

# Moderate changes (3-6 hours)
gh label create "complexity-medium" --color "FFF3CD" --description "Moderate changes, 3-6 hours estimated"

# Complex changes (6+ hours)
gh label create "complexity-high" --color "F8D7DA" --description "Complex changes, 6+ hours estimated"
```

## Usage Examples

### Creating an AI-Ready Issue

```bash
# Create issue with appropriate labels
gh issue create \
  --title "Add logging to country restriction endpoint" \
  --body "Add comprehensive logging to track country restriction decisions for debugging." \
  --label "ai-agent-ready,enhancement,complexity-low,backend"
```

### Best Practices

1. **Consistent Labeling**: Use labels consistently across all issues
2. **Clear Descriptions**: Provide detailed issue descriptions for AI context
3. **Regular Review**: Periodically review and update labels as issues evolve
4. **Team Training**: Ensure team members understand label meanings