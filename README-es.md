# 🛡️ Secure-MCP

> **Capa de ejecución segura para agentes LLM/MCP** — integre agentes de forma segura sin exponer `.env`, secretos o archivos sensibles del sistema.

---

## 🔍 ¿Qué es Secure-MCP?

**Secure-MCP** es un framework middleware centrado en la seguridad que envuelve sus sistemas MCP (Multi-Component Prompting) o Agentes LLM para garantizar que:

- 🚫 `.env`, `claves API`, archivos del sistema y configuraciones privadas **no sean accesibles** por la lógica del agente.
- ✅ Los sistemas MCP/agente aún pueden **realizar operaciones de forma segura**, como llamar APIs o recuperar tokens, a través de un proxy seguro.
- 🧠 Soporta flujos de trabajo LLM, frameworks de agentes (como LangChain, AutoGen, CrewAI) y herramientas basadas en contexto — **sin comprometer la seguridad**.

---

## 🧱 Características Principales

| Característica                  | Descripción                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| 🔐 **SecureEnvBridge**          | Solo se puede acceder a variables de entorno en lista blanca; `.env` no se expone directamente |
| 📂 **Control de Acceso a Archivos** | Bloquea lecturas de archivos como `.env`, `secret.pem`, `key.json`, `config.yaml` etc. |
| 📦 **Proxy de Función Segura**   | Las operaciones sensibles se abstraen en funciones seguras invocables        |
| 📜 **Registro de Auditoría**     | Registra todos los intentos de acceso a recursos sensibles                    |
| 🧪 **Ejecución en Sandbox**      | Opcionalmente ejecuta código MCP en un entorno aislado (ej. Docker, WASM)     |
| ⚙️ **Agnóstico al Framework**    | Fácil de conectar a cualquier sistema de agentes o pipeline LLM               |

---

## 🧰 Caso de Uso de Ejemplo

```python
from secure_mcp.secure_env_bridge import secure_get, secure_open

# Solo se permiten variables de entorno en lista blanca
api_key = secure_get("SERVICE_AUTH_TOKEN")  # ✅ permitido
db_pw = secure_get("DB_PASSWORD")           # ❌ bloqueado

# Apertura segura de archivos (bloquea archivos sensibles)
with secure_open("safe_data.csv") as f:
    content = f.read()
```

Use `SecureEnvBridge` en lugar de `os.getenv()` y `open()` para garantizar la seguridad.

---

## 🔧 Instalación

```bash
git clone https://github.com/yourname/secure-mcp.git
cd secure-mcp
pip install -e .
```

También puede empaquetarlo vía `setup.py` o `pyproject.toml` para despliegue interno en PyPI.

---

## 🛠️ Arquitectura

```txt
[ Entrada de Usuario / Tarea del Agente ]
           ↓
[ SecureContextExecutor ]
           ↓
[ SecureEnvBridge / FileGuard ]
           ↓
[ API Externa, Archivo o Acceso a Memoria ]
           ↓
[ Respuesta del Agente LLM ]
```

* MCP no necesita conocer los secretos.
* SecureEnvBridge actúa como un **delegado consciente del vault**.
* Todo acceso es **controlado, registrado y filtrado**.

---

## 📄 Estructura de Ejemplo

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

## 🚧 Hoja de Ruta

* [x] SecureEnvBridge con cargador de lista blanca
* [x] Guardia de acceso a archivos (parche `open()`)
* [ ] Envoltura de ejecución basada en WASM
* [ ] Ejecutor MCP seguro dockerizado
* [ ] Adaptador proxy OpenAPI
* [ ] Sistema de plugins de agente para LangChain / CrewAI

---

## 🔐 Licencia

Este proyecto está licenciado bajo la **Licencia Apache 2.0**.
Consulte el archivo [LICENSE](./LICENSE) para más detalles.

---

## 🤝 Contribuir

Las solicitudes de extracción son bienvenidas.
Para cambios importantes, primero abra un issue para discutir lo que le gustaría cambiar.
Consulte `CONTRIBUTING.md` para instrucciones detalladas.

---

## 📬 Contacto

¿Preguntas, ideas o comentarios?
No dude en [abrir un issue](https://github.com/yourname/secure-mcp/issues) o iniciar una discusión.