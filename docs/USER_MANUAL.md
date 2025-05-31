# AI Agent System - User Manual

Comprehensive guide for using the AI Agent System in your development workflow.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Daily Usage](#daily-usage)
3. [Configuration](#configuration)
4. [Troubleshooting](#troubleshooting)
5. [Advanced Features](#advanced-features)

## Getting Started

### First Run
```bash
# Initialize and run AI agent
./ai_agent_execute.sh
```

### Understanding Output
- **Task Selection**: AI analyzes GitHub issues
- **Workspace Setup**: Creates isolated environment
- **Implementation**: Makes code changes
- **Patch Generation**: Creates reviewable changes

### Review Process
1. Check patch summary: `cat .ai/patches/task-154-summary.md`
2. Review changes: `git diff --no-index /dev/null .ai/patches/task-154.patch`
3. Apply patch: `git apply .ai/patches/task-154.patch`
4. Test: `php artisan test`
5. Commit: `git commit -m "AI Agent: Task #154"`

## Daily Usage

### Morning Routine
```bash
# Check for new high-priority tasks
./ai_agent_execute.sh --priority=high

# Review overnight patches
ls .ai/patches/*$(date -d "yesterday" +%Y%m%d)*
```

### Task Management
```bash
# Work on specific issue
./ai_agent_execute.sh 154

# Batch process multiple tasks
./ai_agent_execute.sh --batch --max-tasks=3

# Focus on bugs only
./ai_agent_execute.sh --type=bug
```

### Quality Control
```bash
# Validate patches before applying
git apply --check .ai/patches/task-*.patch

# Run tests after applying
php artisan test --coverage

# Check code standards
./vendor/bin/pint --test
```

## Configuration

### GitHub Integration
```bash
# Set up GitHub token
export GITHUB_TOKEN="ghp_your_token_here"

# Add to shell profile
echo 'export GITHUB_TOKEN="ghp_your_token_here"' >> ~/.bashrc
```

### Task Selection
Edit `.ai/config/task_selection.yaml`:
```yaml
task_selection:
  weights:
    priority: 0.35
    complexity: 0.25
    age: 0.15
  filters:
    max_complexity: "medium"
    required_labels: ["ai-agent-ready"]
```

### Enhancement Settings
Edit `.ai/config/enhancement.yaml`:
```yaml
enhancement:
  comment_verbosity: "detailed"
  auto_detect_patterns: true
  quality_gates:
    min_test_coverage: 80
    enforce_psr12: true
```

## Troubleshooting

### Common Issues

**Permission Denied**
```bash
chmod +x ai_agent_execute.sh .ai/scripts/*.sh
```

**No Tasks Found**
```bash
# Add labels to GitHub issues
gh issue edit 154 --add-label "ai-agent-ready"
```

**Patch Conflicts**
```bash
# Use 3-way merge
git apply --3way .ai/patches/task-154.patch
```

**GitHub API Errors**
```bash
# Check token permissions
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
```

### Health Checks
```bash
# System diagnostics
.ai/scripts/health_check.sh

# View logs
tail -f .ai/logs/task_*_$(date +%Y%m%d)*.log

# Check workspace status
cat .ai/securify/.ai-enhanced/reports/workspace_status.md
```

## Advanced Features

### Custom Workflows
```bash
# Create custom filters
echo 'labels: ["shopify"]' > .ai/config/shopify_filter.yaml
./ai_agent_execute.sh --config=shopify_filter
```

### Monitoring
```bash
# Generate reports
python3 .ai/scripts/generate_report.py

# Export statistics
.ai/scripts/export_stats.py --format=json
```

### Integration
```bash
# Slack notifications
export SLACK_WEBHOOK="https://hooks.slack.com/..."
./ai_agent_execute.sh --notify-slack

# CI/CD integration
# See .github/workflows/ai-validation.yml
```

For more detailed information, see the [full documentation](https://github.com/passwordless-OTP/ai-agent-system/docs).