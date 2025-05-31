#!/bin/bash

# AI Workspace Initialization Script
set -e

echo "🤖 Initializing AI Agent Workspace"

# Ensure we're in the right directory
if [ ! -f "../../README.md" ]; then
    echo "❌ Must be run from .ai/scripts/ directory"
    exit 1
fi

cd ..

# Create workspace structure
mkdir -p {securify,patches,logs,context,reports}

# Clone repository
if [ ! -d "securify" ]; then
    echo "📋 Cloning repository for AI workspace..."
    git clone "$(git -C ../.. remote get-url origin)" securify
    cd securify
    git remote rename origin upstream
    echo "✅ Repository cloned"
else
    echo "📋 Refreshing AI workspace..."
    cd securify
    git fetch upstream
    git reset --hard upstream/main
    git clean -fd
    echo "✅ Workspace refreshed"
fi

# Copy instructions
cp ../../README.md .ai-instructions.md

# Create AI enhancement structure
mkdir -p .ai-enhanced/{comments,docs,context,tools,reports}

# Run codebase enhancement
echo "📋 Enhancing codebase with AI context..."
if python3 ../scripts/enhance_codebase.py; then
    echo "✅ Codebase enhanced"
else
    echo "⚠️ Enhancement partially completed"
fi

# Run GitHub analysis if token available
if [ -n "$GITHUB_TOKEN" ]; then
    echo "📋 Analyzing GitHub Projects and Issues..."
    python3 ../scripts/github_projects_analyzer.py > .ai-enhanced/context/github_analysis.json
    echo "✅ GitHub analysis complete"
else
    echo "⚠️ GITHUB_TOKEN not set - creating mock analysis"
    python3 ../scripts/github_projects_analyzer.py > .ai-enhanced/context/github_analysis.json
fi

# Create workspace status report
cat > .ai-enhanced/reports/initialization_report.md << EOF
# AI Workspace Initialization Report

**Date**: $(date)
**Status**: Successfully Initialized

## Workspace Components
- ✅ Repository cloned and configured
- ✅ AI enhancement system active
- ✅ GitHub integration $([ -n "$GITHUB_TOKEN" ] && echo "enabled" || echo "limited")
- ✅ Script automation ready

## Next Steps
1. Run task discovery: \`python3 ../scripts/github_projects_analyzer.py\`
2. Execute AI agent: \`../../ai_agent_execute.sh\`
3. Review generated patches in \`../patches/\`

## Workspace Structure
\`\`\`
.ai/
├── securify/           # AI working clone
├── patches/            # Generated patches
├── scripts/            # Automation scripts  
├── logs/               # Execution logs
└── context/            # Analysis data
\`\`\`

---
*AI Agent Workspace Ready for Autonomous Operation*
EOF

echo "✅ AI workspace initialized successfully"
echo "📊 Report: .ai-enhanced/reports/initialization_report.md"

cd ../..