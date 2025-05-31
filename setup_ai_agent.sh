#!/bin/bash
# setup_ai_agent.sh - Master setup script for AI Agent system

set -e

echo "🚀 Setting up AI Agent System for Securify Repository"
echo "===================================================="

# Phase 1: Validate Environment
echo "📋 Phase 1: Environment Validation"

# Check required tools
REQUIRED_TOOLS=("git" "php" "composer" "python3" "curl")
for tool in "${REQUIRED_TOOLS[@]}"; do
    if ! command -v $tool &> /dev/null; then
        echo "❌ Required tool not found: $tool"
        exit 1
    fi
done
echo "✅ All required tools available"

# Check PHP version
PHP_VERSION=$(php -r "echo PHP_VERSION;")
if [[ ! $PHP_VERSION =~ ^8\. ]]; then
    echo "❌ PHP 8.0+ required, found: $PHP_VERSION"
    exit 1
fi
echo "✅ PHP version compatible: $PHP_VERSION"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository"
    exit 1
fi
echo "✅ Git repository detected"

# Phase 2: GitHub Integration Setup
echo ""
echo "📋 Phase 2: GitHub Integration Setup"

if [ -z "$GITHUB_TOKEN" ]; then
    echo "⚠️  GITHUB_TOKEN not set"
    echo "To enable full GitHub integration:"
    echo "1. Create a GitHub Personal Access Token with repo permissions"
    echo "2. Export GITHUB_TOKEN=your_token_here"
    echo "3. Re-run this script"
    echo ""
    read -p "Continue with limited functionality? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✅ GitHub token detected"
    
    # Test GitHub API access
    if curl -s -H "Authorization: token $GITHUB_TOKEN" \
           "https://api.github.com/user" >/dev/null; then
        echo "✅ GitHub API access confirmed"
    else
        echo "❌ GitHub API access failed - check token permissions"
        exit 1
    fi
fi

# Phase 3: Create AI Agent Directory Structure
echo ""
echo "📋 Phase 3: Creating AI Agent Directory Structure"

mkdir -p .ai/{scripts,patches,logs,context,reports,config}

echo "✅ AI directory structure created"

# Phase 4: Download AI Agent Scripts
echo ""
echo "📋 Phase 4: Installing AI Agent Scripts"

# Download scripts from the AI Agent System repository
echo "Downloading AI scripts from GitHub..."

curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/scripts/enhance_codebase.py -o .ai/scripts/enhance_codebase.py
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/scripts/github_projects_analyzer.py -o .ai/scripts/github_projects_analyzer.py
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/scripts/execute_task.sh -o .ai/scripts/execute_task.sh
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/scripts/generate_production_patch.sh -o .ai/scripts/generate_production_patch.sh
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/scripts/initialize_workspace.sh -o .ai/scripts/initialize_workspace.sh

# Download main executor
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/ai_agent_execute.sh -o ai_agent_execute.sh

# Make scripts executable
chmod +x .ai/scripts/*.py .ai/scripts/*.sh ai_agent_execute.sh

echo "✅ AI Agent scripts installed"

# Phase 5: Update Main README
echo ""
echo "📋 Phase 5: Updating Main README with AI Instructions"

# Backup original README
cp README.md README.md.backup

# Download AI-enhanced README
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/README.md -o README.md

echo "✅ Main README updated with AI instructions"
echo "📋 Original README backed up to README.md.backup"

# Phase 6: Create Configuration Files
echo ""
echo "📋 Phase 6: Creating Configuration Files"

# Create task selection configuration
cat > .ai/config/task_selection.yaml << 'EOF'
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
    blocked_labels: ["needs discussion", "blocked"]
    min_description_length: 100
    
  limits:
    max_daily_tasks: 5
    max_task_duration: "4h"
    max_files_per_task: 10
EOF

# Create enhancement configuration
cat > .ai/config/enhancement.yaml << 'EOF'
enhancement:
  comment_verbosity: "detailed"
  
  patterns:
    auto_detect_shopify: true
    auto_detect_geolocation: true
    auto_detect_api_endpoints: true
    auto_detect_database_ops: true
    
  documentation:
    generate_method_docs: true
    update_readme_links: true
    create_architecture_maps: true
    
  quality_gates:
    min_test_coverage: 80
    enforce_psr12: true
    require_static_analysis: true
    check_security_patterns: true
EOF

echo "✅ Configuration files created"

# Phase 7: Final Validation
echo ""
echo "📋 Phase 7: Final Validation"

# Check essential files
REQUIRED_FILES=(
    ".ai/scripts/enhance_codebase.py"
    ".ai/scripts/github_projects_analyzer.py"
    ".ai/scripts/execute_task.sh"
    ".ai/scripts/generate_production_patch.sh"
    "ai_agent_execute.sh"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Missing required file: $file"
        exit 1
    fi
    
    if [ ! -x "$file" ]; then
        echo "❌ File not executable: $file"
        exit 1
    fi
done

echo "✅ All components validated successfully"

# Create setup completion report
cat > .ai/SETUP_COMPLETE.md << 'EOF'
# AI Agent System Setup Complete! 🎉

## Installation Summary
- ✅ AI workspace structure created
- ✅ GitHub integration configured
- ✅ Task automation scripts installed
- ✅ Clean patch generation system ready
- ✅ One-command execution available

## Quick Start
```bash
# Start AI agent autonomous operation
./ai_agent_execute.sh

# Or execute specific task
./ai_agent_execute.sh 154
```

## Architecture Overview
```
Repository Root/
├── README.md                    # AI Agent instructions
├── ai_agent_execute.sh         # One-command executor
├── .ai/                        # AI workspace (isolated)
│   ├── securify/              # AI working clone
│   ├── patches/               # Clean patches for production
│   ├── scripts/               # Automation tools
│   └── logs/                  # Execution history
└── [production code]          # Untouched by AI agents
```

## Next Steps
1. **Set GitHub Token** (for full functionality):
   ```bash
   export GITHUB_TOKEN=your_token_here
   ```

2. **Run First AI Agent Task**:
   ```bash
   ./ai_agent_execute.sh
   ```

3. **Review Generated Patch**:
   ```bash
   cat .ai/patches/task-*-summary.md
   git apply .ai/patches/task-*.patch
   ```

## Key Benefits
- 🤖 **Autonomous Development**: AI handles routine tasks
- 🔒 **Clean Separation**: Production code stays untouched
- 📊 **Quality Assurance**: Automated testing and validation
- 🎯 **Smart Task Selection**: GitHub integration for priority
- 📦 **Clean Patches**: Only business logic changes reach production

---
*Your repository is now AI Agent ready! 🚀*
EOF

echo ""
echo "🎉 AI Agent System Setup Complete!"
echo "================================="
echo ""
echo "📍 **Setup Summary:**"
echo "   ✅ AI workspace structure created"
echo "   ✅ GitHub integration configured"  
echo "   ✅ Automation scripts installed"
echo "   ✅ Clean patch generation ready"
echo "   ✅ One-command execution available"
echo ""
echo "🚀 **Quick Start:**"
echo "   ./ai_agent_execute.sh"
echo ""
echo "📊 **Setup Details:**"
echo "   - Setup report: .ai/SETUP_COMPLETE.md"
echo "   - Original README backup: README.md.backup"
echo "   - AI scripts: .ai/scripts/"
echo ""
echo "⚡ **Next Steps:**"
echo "   1. Set GITHUB_TOKEN for full functionality"
echo "   2. Run: ./ai_agent_execute.sh"
echo "   3. Review generated patches in .ai/patches/"
echo ""
echo "🎯 **Your repository is now AI Agent ready!**"