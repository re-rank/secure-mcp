# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-07-21

### Added
- Initial release of Secure-MCP
- `secure_get()` function for whitelisted environment variable access
- `secure_open()` function for secure file access with path filtering
- Audit logging system that records all access attempts
- Whitelist management for environment variables
- Blocked file patterns for sensitive files (.env, *.key, *.pem, etc.)
- Blocked path patterns for sensitive directories (/etc/secrets/, ~/.ssh/, etc.)
- Basic example demonstrating usage
- Full documentation and contribution guidelines
- Multi-language README support (EN, KO, JA, ZH, ES)