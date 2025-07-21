"""
Whitelist management for allowed environment variables and file patterns
"""

import json
from pathlib import Path
from typing import List, Set

WHITELIST_KEYS = [
    "SERVICE_AUTH_TOKEN",
    "PUBLIC_API_KEY", 
    "USER_AGENT_NAME",
    "PUBLIC_CONFIG",
    "APP_VERSION",
    "NODE_ENV",
    "PYTHON_ENV"
]

BLOCKED_FILE_PATTERNS = [
    ".env",
    ".env.*",
    "*.pem",
    "*.key",
    "*.crt",
    "id_rsa*",
    "id_dsa*",
    "id_ecdsa*",
    "id_ed25519*",
    "config.json",
    "credentials.json",
    "secrets.json",
    "*.p12",
    "*.pfx",
    "authorized_keys",
    "known_hosts"
]

BLOCKED_PATH_PATTERNS = [
    "/etc/secrets/",
    "/etc/security/",
    "~/.ssh/",
    ".ssh/",
    "/root/",
    "/.aws/",
    "/.kube/",
    "/.docker/"
]


def get_env_whitelist() -> Set[str]:
    """
    Get the set of whitelisted environment variable keys
    
    Returns:
        Set of allowed environment variable names
    """
    config_file = Path("config/whitelist.json")
    
    if config_file.exists():
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                return set(config.get("env_whitelist", WHITELIST_KEYS))
        except (json.JSONDecodeError, KeyError):
            pass
    
    return set(WHITELIST_KEYS)


def is_file_blocked(filepath: str) -> bool:
    """
    Check if a file path matches any blocked patterns
    
    Args:
        filepath: Path to check
        
    Returns:
        True if the file is blocked, False otherwise
    """
    path = Path(filepath)
    filename = path.name
    abs_path = str(path.absolute())
    
    for pattern in BLOCKED_FILE_PATTERNS:
        if pattern.startswith("*"):
            if filename.endswith(pattern[1:]):
                return True
        elif pattern.endswith("*"):
            if filename.startswith(pattern[:-1]):
                return True
        elif filename == pattern:
            return True
    
    for blocked_path in BLOCKED_PATH_PATTERNS:
        if blocked_path in abs_path:
            return True
            
    return False