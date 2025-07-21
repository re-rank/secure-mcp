"""
Secure environment variable access with whitelist filtering
"""

import os
from typing import Optional

from .audit_logger import log_env_access
from .whitelist_loader import get_env_whitelist


def secure_get(key: str) -> Optional[str]:
    """
    Securely get environment variable value with whitelist filtering
    
    Args:
        key: Environment variable key to retrieve
        
    Returns:
        Environment variable value if allowed, None if not set
        
    Raises:
        AccessDenied: If the key is not in the whitelist
    """
    whitelist = get_env_whitelist()
    
    if key not in whitelist:
        log_env_access(key, allowed=False)
        from . import AccessDenied
        raise AccessDenied(f"Access denied: Environment variable '{key}' is not whitelisted")
    
    value = os.environ.get(key)
    log_env_access(key, allowed=True)
    
    return value