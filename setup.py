"""
Setup configuration for Secure-MCP
"""

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="secure-mcp",
    version="0.1.0",
    author="re-rank",
    author_email="hojinpark@re-rank.com",
    description="Secure execution layer for LLM/MCP agents - prevent unauthorized access to sensitive files and environment variables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/re-rank/secure-mcp",
    project_urls={
        "Bug Tracker": "https://github.com/yourname/secure-mcp/issues",
        "Documentation": "https://github.com/yourname/secure-mcp/wiki",
        "Source Code": "https://github.com/yourname/secure-mcp",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies required for basic functionality
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=5.0",
            "mypy>=1.0",
        ],
    },
    keywords="security mcp llm agent sandbox whitelist audit",
)