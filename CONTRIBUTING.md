# Contributing to AI Agent System

We welcome contributions to the AI Agent System! This document provides guidelines for contributing.

## Getting Started

### Development Setup

```bash
# Clone the repository
git clone https://github.com/passwordless-OTP/ai-agent-system.git
cd ai-agent-system

# Create development environment
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python3 -m pytest tests/
```

### Development Environment

- **Python**: 3.8 or higher
- **Bash**: For shell scripts
- **Git**: For version control
- **GitHub CLI**: For testing GitHub integration

## Contribution Areas

### 🐛 Bug Fixes
- Fix issues reported in GitHub Issues
- Improve error handling and edge cases
- Enhance system reliability

### 🔧 New Features
- Add support for new frameworks
- Enhance AI capabilities
- Improve GitHub integration
- Add new quality gates

### 📚 Documentation
- Improve user guides
- Add examples and tutorials
- Update API documentation
- Create video tutorials

### 🧪 Testing
- Expand test coverage
- Add integration tests
- Create performance benchmarks
- Test edge cases

### 🎨 User Experience
- Improve command-line interface
- Enhance error messages
- Add progress indicators
- Improve configuration options

## Development Guidelines

### Code Style

#### Python
- Follow PEP 8 style guide
- Use type hints where appropriate
- Maximum line length: 88 characters
- Use meaningful variable names

```python
# Good
def analyze_github_issues(repository: str, token: str) -> Dict[str, Any]:
    """Analyze GitHub issues for AI readiness."""
    pass

# Avoid
def analyze(repo, tok):
    pass
```

#### Bash
- Use `set -e` for error handling
- Quote variables: `"$VARIABLE"`
- Use meaningful function names
- Add comments for complex logic

```bash
#!/bin/bash
set -e

# Good
function validate_github_token() {
    local token="$1"
    curl -sf -H "Authorization: token $token" https://api.github.com/user >/dev/null
}
```

### Testing

#### Unit Tests
```bash
# Run all tests
python3 -m pytest

# Run specific test file
python3 -m pytest tests/test_github_analyzer.py

# Run with coverage
python3 -m pytest --cov=scripts
```

#### Integration Tests
```bash
# Test full workflow
./tests/integration/test_full_workflow.sh

# Test GitHub integration
GITHUB_TOKEN="$GITHUB_TOKEN" ./tests/integration/test_github.sh
```

### Documentation

- Update README.md for user-facing changes
- Add docstrings to Python functions
- Update CHANGELOG.md for all changes
- Include examples for new features

## Submission Process

### 1. Create an Issue

Before starting work, create or comment on a GitHub issue to:
- Describe the problem or enhancement
- Discuss the approach
- Get feedback from maintainers

### 2. Fork and Branch

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/ai-agent-system.git
cd ai-agent-system

# Create feature branch
git checkout -b feature/your-feature-name
```

### 3. Develop and Test

```bash
# Make changes
# ...

# Run tests
python3 -m pytest

# Test installation
./tests/test_installation.sh

# Test with real repository (if applicable)
cd /tmp/test-repo
bash /path/to/ai-agent-system/setup_ai_agent.sh
```

### 4. Commit Guidelines

Use conventional commit format:

```bash
# Format: type(scope): description

# Examples:
git commit -m "feat(github): add project board integration"
git commit -m "fix(setup): handle missing GitHub token gracefully"
git commit -m "docs(readme): update installation instructions"
git commit -m "test(analyzer): add unit tests for task prioritization"
```

#### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Maintenance tasks

### 5. Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create PR via GitHub UI or CLI
gh pr create --title "Add project board integration" \
             --body "Adds support for GitHub project boards with automatic column detection."
```

#### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Breaking change

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

## Review Process

### Code Review

1. **Automated Checks**: All CI checks must pass
2. **Peer Review**: At least one maintainer review
3. **Testing**: Manual testing by reviewer if needed
4. **Documentation**: Verify docs are updated

### Review Criteria

- **Functionality**: Does it work as intended?
- **Code Quality**: Is it readable and maintainable?
- **Testing**: Are there adequate tests?
- **Documentation**: Is it properly documented?
- **Compatibility**: Does it maintain backward compatibility?

## Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

1. Update version numbers
2. Update CHANGELOG.md
3. Run full test suite
4. Create release tag
5. Update documentation
6. Announce release

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Focus on what's best for the community

### Communication

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code review and collaboration

### Getting Help

- Check existing issues and documentation first
- Provide detailed information when asking for help
- Be patient - this is a community project

## Recognition

Contributors are recognized in:
- README.md contributors section
- Release notes
- Git commit history
- Special recognition for significant contributions

---

Thank you for contributing to the AI Agent System! Your efforts help make autonomous development accessible to everyone.