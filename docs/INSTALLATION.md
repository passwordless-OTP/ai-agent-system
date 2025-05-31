# Installation Guide

## Quick Installation

### One-Command Setup
```bash
curl -fsSL https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/setup_ai_agent.sh | bash
```

### Manual Installation

1. **Download the setup script**
```bash
curl -o setup_ai_agent.sh https://raw.githubusercontent.com/passwordless-OTP/ai-agent-system/main/setup_ai_agent.sh
chmod +x setup_ai_agent.sh
```

2. **Run the installer**
```bash
./setup_ai_agent.sh
```

## Prerequisites

- **PHP**: 8.0 or higher
- **Git**: 2.20 or higher  
- **Python**: 3.8 or higher
- **Composer**: Latest version
- **GitHub Token**: Personal access token with repo permissions

## Verification

```bash
# Test the installation
./ai_agent_execute.sh --verify

# Check GitHub integration
export GITHUB_TOKEN="your_token_here"
python3 .ai/scripts/github_projects_analyzer.py
```

## Next Steps

1. Set up GitHub token
2. Add AI labels to your issues
3. Run your first AI task: `./ai_agent_execute.sh`