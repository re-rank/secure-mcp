"""
Basic example demonstrating secure environment variable and file access
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from secure_env_bridge import secure_get, secure_open, AccessDenied


def demo_env_access():
    """Demonstrate secure environment variable access"""
    print("=== Environment Variable Access Demo ===\n")
    
    test_keys = [
        "SERVICE_AUTH_TOKEN",
        "DB_PASSWORD", 
        "PUBLIC_API_KEY",
        "SECRET_KEY",
        "USER_AGENT_NAME"
    ]
    
    for key in test_keys:
        try:
            value = secure_get(key)
            if value:
                print(f"[OK] {key}: {value[:10]}... (truncated)")
            else:
                print(f"[OK] {key}: Not set")
        except AccessDenied as e:
            print(f"[DENIED] {key}: {e}")
    
    print()


def demo_file_access():
    """Demonstrate secure file access"""
    print("=== File Access Demo ===\n")
    
    test_files = [
        "safe_data.csv",
        ".env",
        "config.json",
        "id_rsa",
        "example.txt",
        "/etc/secrets/api_key.pem"
    ]
    
    for filepath in test_files:
        try:
            with secure_open(filepath, 'r') as f:
                content = f.read(50)
                print(f"[OK] {filepath}: Successfully opened")
        except AccessDenied as e:
            print(f"[DENIED] {filepath}: {e}")
        except FileNotFoundError:
            print(f"[WARNING] {filepath}: File not found (but access would be allowed)")
        except Exception as e:
            print(f"[WARNING] {filepath}: {type(e).__name__}: {e}")
    
    print()


def create_test_file():
    """Create a test file for demonstration"""
    test_file = "example.txt"
    if not os.path.exists(test_file):
        with open(test_file, 'w') as f:
            f.write("This is a safe file that can be accessed.\n")
        print(f"Created test file: {test_file}")


if __name__ == "__main__":
    print("Secure-MCP Example: Demonstrating secure access controls\n")
    
    os.environ["SERVICE_AUTH_TOKEN"] = "dummy-token-12345"
    os.environ["DB_PASSWORD"] = "super-secret-password"
    os.environ["PUBLIC_API_KEY"] = "pk_test_12345"
    
    create_test_file()
    
    demo_env_access()
    demo_file_access()
    
    print("\n[INFO] Check logs/access.log for audit trail")