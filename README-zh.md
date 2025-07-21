# 🛡️ Secure-MCP

> **LLM/MCP代理的安全执行层** — 安全集成代理而不暴露`.env`、密钥或敏感系统文件。

---

## 🔍 什么是Secure-MCP？

**Secure-MCP**是一个以安全为中心的中间件框架，它包装您的MCP（多组件提示）或LLM代理系统，以确保：

- 🚫 `.env`、`API密钥`、系统文件和私有配置对代理逻辑**不可访问**。
- ✅ MCP/代理系统仍可通过安全代理**安全执行操作**，如调用API或检索令牌。
- 🧠 支持LLM工作流、代理框架（如LangChain、AutoGen、CrewAI）和基于上下文的工具 — **不会损害安全性**。

---

## 🧱 主要特性

| 特性                          | 描述                                                                    |
|------------------------------|-------------------------------------------------------------------------|
| 🔐 **SecureEnvBridge**        | 只能访问白名单环境变量；`.env`不会直接暴露                                   |
| 📂 **文件访问控制**            | 阻止读取如`.env`、`secret.pem`、`key.json`、`config.yaml`等文件           |
| 📦 **安全函数代理**            | 将敏感操作抽象为安全的可调用函数                                            |
| 📜 **审计日志**               | 记录所有访问敏感资源的尝试                                                 |
| 🧪 **沙盒执行**               | 可选择在隔离环境（如Docker、WASM）中运行MCP代码                             |
| ⚙️ **框架无关**               | 易于插入任何代理系统或LLM管道                                              |

---

## 🧰 使用示例

```python
from secure_mcp.secure_env_bridge import secure_get, secure_open

# 只允许白名单环境变量
api_key = secure_get("SERVICE_AUTH_TOKEN")  # ✅ 允许
db_pw = secure_get("DB_PASSWORD")           # ❌ 阻止

# 安全文件打开（阻止敏感文件）
with secure_open("safe_data.csv") as f:
    content = f.read()
```

使用`SecureEnvBridge`代替`os.getenv()`和`open()`以确保安全。

---

## 🔧 安装

```bash
git clone https://github.com/yourname/secure-mcp.git
cd secure-mcp
pip install -e .
```

您也可以通过`setup.py`或`pyproject.toml`打包以进行内部PyPI部署。

---

## 🛠️ 架构

```txt
[ 用户输入 / 代理任务 ]
           ↓
[ SecureContextExecutor ]
           ↓
[ SecureEnvBridge / FileGuard ]
           ↓
[ 外部API、文件或内存访问 ]
           ↓
[ LLM代理响应 ]
```

* MCP不需要知道密钥。
* SecureEnvBridge充当**保险库感知代理**。
* 每次访问都被**控制、记录和过滤**。

---

## 📄 示例结构

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

## 🚧 路线图

* [x] 带白名单加载器的SecureEnvBridge
* [x] 文件访问守卫（`open()`补丁）
* [ ] 基于WASM的执行包装器
* [ ] Docker化的安全MCP运行器
* [ ] OpenAPI代理适配器
* [ ] LangChain / CrewAI的代理插件系统

---

## 🔐 许可证

本项目根据**Apache License 2.0**许可。
详见[LICENSE](./LICENSE)文件。

---

## 🤝 贡献

欢迎提交拉取请求。
对于重大更改，请先开启一个问题讨论您想要更改的内容。
详细说明请查看`CONTRIBUTING.md`。

---

## 📬 联系方式

有问题、想法或反馈？
欢迎[开启问题](https://github.com/yourname/secure-mcp/issues)或开始讨论。