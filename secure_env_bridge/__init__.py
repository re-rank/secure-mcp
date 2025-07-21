"""
Secure-MCP: Security layer for LLM/MCP agents
Prevents unauthorized access to sensitive environment variables and files
"""

from .secure_get import secure_get
from .secure_open import secure_open

__all__ = ['secure_get', 'secure_open']

class AccessDenied(Exception):
    """Exception raised when attempting to access restricted resources"""
    pass