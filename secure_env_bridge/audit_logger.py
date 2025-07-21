"""
Audit logging system for tracking access attempts to sensitive resources
"""

import os
import logging
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_FILE = LOG_DIR / "access.log"

LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def log_env_access(key: str, allowed: bool) -> None:
    """
    Log environment variable access attempts
    
    Args:
        key: The environment variable key that was accessed
        allowed: Whether the access was allowed or denied
    """
    timestamp = datetime.now().isoformat()
    log_message = f"[ENV ACCESS] key={key} allowed={allowed} at {timestamp}"
    logger.info(log_message)


def log_file_access(path: str, allowed: bool) -> None:
    """
    Log file access attempts
    
    Args:
        path: The file path that was accessed
        allowed: Whether the access was allowed or denied
    """
    timestamp = datetime.now().isoformat()
    log_message = f"[FILE ACCESS] file={path} allowed={allowed} at {timestamp}"
    logger.info(log_message)