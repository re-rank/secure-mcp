# Contributing to Secure-MCP

Thank you for your interest in contributing to Secure-MCP! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:
- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive criticism
- Respect differing viewpoints and experiences

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourname/secure-mcp/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version)
   - Any relevant logs or screenshots

### Suggesting Features

1. Check existing [Issues](https://github.com/yourname/secure-mcp/issues) for similar suggestions
2. Create a new issue with:
   - Clear description of the feature
   - Use cases and benefits
   - Potential implementation approach

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add or update tests as needed
5. Ensure all tests pass (`pytest`)
6. Format code with Black (`black secure_env_bridge/`)
7. Commit with clear message (`git commit -m 'Add amazing feature'`)
8. Push to your fork (`git push origin feature/amazing-feature`)
9. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/secure-mcp.git
cd secure-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8 secure_env_bridge/
mypy secure_env_bridge/

# Format code
black secure_env_bridge/
```

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for high test coverage
- Test edge cases and error conditions

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=secure_env_bridge

# Run specific test file
pytest tests/test_secure_get.py
```

## Code Style

- Follow PEP 8
- Use Black for formatting
- Add type hints where possible
- Write clear, descriptive variable names
- Add docstrings to all public functions/classes

## Documentation

- Update README.md if needed
- Add docstrings following Google style
- Include examples in docstrings
- Update CHANGELOG.md for notable changes

## Security

- Never commit sensitive data
- Test security features thoroughly
- Consider edge cases and attack vectors
- Report security issues privately to maintainers

## Questions?

Feel free to open an issue for any questions about contributing!