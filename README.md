# 🛡️ Secure-MCP

> **Secure execution layer for LLM/MCP agents** — safely integrate agents without exposing `.env`, secrets, or sensitive system files.

---

## 🔍 What is Secure-MCP?

**Secure-MCP** is a security-focused middleware framework that wraps around your MCP (Multi-Component Prompting) or LLM Agent systems to ensure that:

- 🚫 `.env`, `API keys`, system files, and private configs are **not accessible** by agent logic.
- ✅ MCP/agent systems can still **safely perform operations**, such as calling APIs or retrieving tokens, via a secure proxy.
- 🧠 It supports LLM workflows, agent frameworks (like LangChain, AutoGen, CrewAI), and context-based tools — **without compromising security**.

---

## 🧱 Key Features

| Feature                         | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| 🔐 **SecureEnvBridge**          | Only whitelisted env variables can be accessed; `.env` is not directly exposed |
| 📂 **File Access Control**       | Blocks file reads like `.env`, `secret.pem`, `key.json`, `config.yaml` etc. |
| 📦 **Secure Function Proxy**     | Sensitive operations are abstracted into secured callable functions         |
| 📜 **Audit Logging**            | Logs all attempts to access sensitive resources                             |
| 🧪 **Sandboxed Execution**       | Optionally runs MCP code in an isolated environment (e.g., Docker, WASM)     |
| ⚙️ **Framework Agnostic**         | Easy to plug into any agent system or LLM pipeline                          |

---

## 🧰 Example Use Case

```python
from secure_mcp.secure_env_bridge import secure_get, secure_open

# Only whitelisted environment variables are allowed
api_key = secure_get("SERVICE_AUTH_TOKEN")  # ✅ allowed
db_pw = secure_get("DB_PASSWORD")           # ❌ blocked

# Safe file open (blocks sensitive files)
with secure_open("safe_data.csv") as f:
    content = f.read()
```

Use `SecureEnvBridge` instead of `os.getenv()` and `open()` to ensure safety.

---

## 🔧 Installation

```bash
git clone https://github.com/yourname/secure-mcp.git
cd secure-mcp
pip install -e .
```

You may also package it via `setup.py` or `pyproject.toml` for internal PyPI deployment.

---

## 🛠️ Architecture

```txt
[ User Input / Agent Task ]
           ↓
[ SecureContextExecutor ]
           ↓
[ SecureEnvBridge / FileGuard ]
           ↓
[ External API, File, or Memory Access ]
           ↓
[ LLM Agent Response ]
```

* MCP doesn't need to know the secrets.
* SecureEnvBridge acts like a **vault-aware delegate**.
* Every access is **controlled, logged, and filtered**.

---

## 📄 Example Structure

```
secure-mcp/
├── secure_env_bridge/
│   ├── secure_get.py
│   ├── secure_open.py
│   ├── whitelist_loader.py
│   └── audit_logger.py
├── examples/
│   ├── fastapi_demo.py
│   └── sandbox_runner.py
├── tests/
│   └── test_env_guard.py
├── .env.example
├── LICENSE
├── README.md
└── setup.py
```

---

## 🚧 Roadmap

* [x] SecureEnvBridge with whitelist loader
* [x] File access guard (`open()` patch)
* [ ] WASM-based execution wrapper
* [ ] Dockerized secure MCP runner
* [ ] OpenAPI proxy adapter
* [ ] Agent plugin system for LangChain / CrewAI

---

## 🔐 License

This project is licensed under the **Apache License 2.0**.
See the [LICENSE](./LICENSE) file for more details.

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.
Check `CONTRIBUTING.md` for detailed instructions.

---

## 📬 Contact

Questions, ideas, or feedback?
Feel free to [open an issue](https://github.com/yourname/secure-mcp/issues) or start a discussion.