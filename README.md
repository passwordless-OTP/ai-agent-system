# AI Agent System (AIAS)

> **Autonomous Development Assistant for Laravel/PHP Projects**

The AI Agent System enables autonomous task discovery, execution, and patch generation while maintaining clean separation between AI workspace and production code.

## 🚀 Quick Start

### One-Command Installation
```bash
# Navigate to your repository
cd /path/to/your/laravel/project

# Install AI Agent System
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/setup_ai_agent.sh | bash

# Run AI agent
./ai_agent_execute.sh
```

### What This Does
1. **Analyzes GitHub Issues/Projects** for AI-ready tasks
2. **Creates isolated AI workspace** in `.ai/` directory  
3. **Implements solutions** with comprehensive context
4. **Generates clean patches** for human review
5. **Maintains production code integrity** - no AI pollution

## 🏠 Architecture

```
project-root/
├── README.md                 # Updated with AI instructions
├── ai_agent_execute.sh      # One-command executor
├── .ai/                     # AI workspace (isolated)
│   ├── securify/           # AI working clone with context
│   ├── patches/            # Clean patches for production
│   ├── scripts/            # AI automation tools
│   └── logs/               # Execution history
└── [production code]        # Untouched by AI agents
```

## 🤖 Key Features

### 🔒 **Clean Separation**
- Production code remains **completely untouched**
- AI works in isolated `.ai/` workspace
- Only validated business logic reaches production

### 📊 **GitHub Integration**
- Automatic task discovery from Issues and Project boards
- Smart prioritization based on labels and complexity
- Respects dependencies and blocking relationships

### 🔍 **Quality Assurance**
- Full test suite execution in AI workspace
- Code standards validation (PSR-12)
- Security and performance impact analysis
- Comprehensive change documentation

### 👥 **Human Control**
- Manual review and approval of all changes
- Detailed patch summaries with risk assessment
- Easy rollback and modification capabilities

## 📝 Usage Examples

### Basic Usage
```bash
# Let AI select optimal task
./ai_agent_execute.sh

# Work on specific GitHub issue
./ai_agent_execute.sh 154

# Review AI results
cat .ai/patches/task-154-summary.md

# Apply to production
git apply .ai/patches/task-154-20250531.patch
php artisan test
git commit -m "AI Agent: Fix endpoints (Issue #154)"
```

### Task Management
```bash
# Analyze current GitHub state
python3 .ai/scripts/github_projects_analyzer.py

# Focus on high-priority tasks
./ai_agent_execute.sh --priority=high

# Process multiple tasks
./ai_agent_execute.sh --batch --max-tasks=3
```

## 🏷️ GitHub Labels for AI

Add these labels to your GitHub repository for optimal AI task management:

### Priority Labels
- `high priority` - Work on this first
- `medium priority` - Standard priority
- `low priority` - Lower priority

### AI Readiness
- `ai-agent-ready` - Explicitly marked for AI
- `good first issue` - Simple tasks for AI
- `help wanted` - Community/AI assistance welcome

### Complexity Estimation
- `complexity-low` - Simple changes (1-2 hours)
- `complexity-medium` - Moderate changes (3-6 hours)  
- `complexity-high` - Complex changes (6+ hours)

### Blocking Labels
- `needs discussion` - Requires human input
- `blocked` - Cannot proceed
- `waiting for input` - Awaiting information

## ⚙️ Configuration

### GitHub Token Setup
```bash
# Create GitHub Personal Access Token with 'repo' permissions
export GITHUB_TOKEN="ghp_your_token_here"

# Add to shell profile for persistence
echo 'export GITHUB_TOKEN="ghp_your_token_here"' >> ~/.bashrc
```

### Task Selection Tuning
```yaml
# .ai/config/task_selection.yaml
task_selection:
  weights:
    priority: 0.35
    complexity: 0.25
    age: 0.15
    dependencies: 0.15
    project_context: 0.1
  
  filters:
    max_complexity: "medium"
    required_labels: ["ai-agent-ready"]
    blocked_labels: ["needs discussion"]
```

## 🔍 Quality Gates

Every AI-generated patch includes:

### Automated Testing
- ✅ Full PHPUnit test suite
- ✅ Code coverage maintenance
- ✅ Integration test validation

### Code Quality
- ✅ PSR-12 coding standards
- ✅ PHPStan static analysis
- ✅ Security pattern checking

### Documentation
- ✅ Change impact analysis
- ✅ Risk assessment
- ✅ Manual testing instructions

## 🛠️ Troubleshooting

### Common Issues

**AI agent won't start:**
```bash
# Check permissions
chmod +x ai_agent_execute.sh .ai/scripts/*.sh

# Verify environment
php --version  # Need PHP 8.0+
git --version  # Need Git 2.20+
```

**No tasks found:**
```bash
# Check GitHub token
echo $GITHUB_TOKEN
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user

# Add AI-ready labels to issues
gh issue edit 154 --add-label "ai-agent-ready"
```

**Patch won't apply:**
```bash
# Check for conflicts
git apply --check .ai/patches/task-154-*.patch

# Force 3-way merge if needed
git apply --3way .ai/patches/task-154-*.patch
```

### Health Check
```bash
# Run system diagnostics
.ai/scripts/health_check.sh

# View recent activity
ls -la .ai/logs/
cat .ai/patches/task-*-summary.md
```

## 🔄 Workflow Integration

### CI/CD Integration
```yaml
# .github/workflows/ai-validation.yml
name: AI Patch Validation
on:
  push:
    paths: ['.ai/patches/**']

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Apply and test AI patches
        run: |
          git apply .ai/patches/*.patch
          php artisan test
```

### Team Collaboration
```bash
# Morning routine: process overnight issues
./ai_agent_execute.sh --batch

# Review team patches
ls .ai/patches/*$(date +%Y%m%d)*

# Apply validated changes
for patch in .ai/patches/task-*.patch; do
  git apply "$patch" && git commit -m "AI: $(basename $patch .patch)"
done
```

## 📈 Benefits

### For Developers
- 🤖 **Autonomous task handling** - Focus on complex work
- 🔒 **Zero production risk** - Clean workspace separation
- 📊 **Quality assurance** - Automated testing and validation
- ⏱️ **Time savings** - Routine tasks handled automatically

### For Teams
- 🎯 **Consistent quality** - Standardized code patterns
- 📅 **Faster delivery** - Parallel AI development
- 📊 **Better tracking** - Comprehensive change documentation
- 👥 **Team scaling** - AI handles routine work

### For Projects
- 🚀 **Velocity increase** - More features delivered faster
- 🔧 **Maintenance reduction** - AI handles technical debt
- 📈 **Quality improvement** - Consistent patterns and testing
- 💰 **Cost efficiency** - Reduced manual development time

## 🔗 Advanced Features

### Batch Processing
```bash
# Process all high-priority tasks
./ai_agent_execute.sh --priority=high --batch

# Work on specific project board column
./ai_agent_execute.sh --project-column="Ready for Development"

# Focus on bug fixes only
./ai_agent_execute.sh --type=bug --max-tasks=5
```

### Custom Workflows
```bash
# Create custom task filters
echo 'labels: ["shopify", "geolocation"]' > .ai/config/custom_filter.yaml
./ai_agent_execute.sh --config=custom_filter

# Integration with external tools
./ai_agent_execute.sh --notify-slack --update-jira
```

### Monitoring and Analytics
```bash
# Generate activity reports
python3 .ai/scripts/generate_report.py --since="7 days ago"

# Monitor AI performance
.ai/scripts/performance_analyzer.py --metrics

# Export patch statistics
.ai/scripts/export_stats.py --format=csv
```

## 🤝 Contributing

We welcome contributions to improve the AI Agent System!

### Development Setup
```bash
# Clone the repository
git clone https://github.com/passwordless-OTP/ai-agent-system.git
cd ai-agent-system

# Create development environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
python3 -m pytest tests/
```

### Contribution Areas
- 🐛 **Bug Fixes** - Help improve reliability
- 🔧 **New Features** - Add AI capabilities
- 📚 **Documentation** - Improve user guides
- 🧪 **Testing** - Expand test coverage
- 🎨 **UI/UX** - Enhance user experience

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🆘 Support

- 📖 **Documentation**: [Full User Manual](docs/USER_MANUAL.md)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/passwordless-OTP/ai-agent-system/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/passwordless-OTP/ai-agent-system/discussions)
- 📧 **Email**: support@ai-agent-system.dev

---

**Ready to supercharge your development workflow?**

```bash
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/setup_ai_agent.sh | bash
```

*Transform your repository into an AI-powered development environment in minutes!*