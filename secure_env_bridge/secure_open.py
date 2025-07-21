"""
Secure file access with path filtering
"""

from typing import IO, Any, Optional
import os

from .audit_logger import log_file_access
from .whitelist_loader import is_file_blocked


def secure_open(filepath: str, mode: str = 'r', **kwargs) -> IO[Any]:
    """
    Securely open a file with path filtering to prevent access to sensitive files
    
    Args:
        filepath: Path to the file to open
        mode: File open mode (default: 'r')
        **kwargs: Additional arguments to pass to open()
        
    Returns:
        File object if allowed
        
    Raises:
        AccessDenied: If the file path matches blocked patterns
    """
    abs_path = os.path.abspath(filepath)
    
    if is_file_blocked(filepath):
        log_file_access(filepath, allowed=False)
        from . import AccessDenied
        raise AccessDenied(f"AccessDenied: Attempted to open restricted file: {filepath}")
    
    log_file_access(filepath, allowed=True)
    
    return open(abs_path, mode, **kwargs)