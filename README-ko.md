# 🛡️ Secure-MCP

> **LLM/MCP 에이전트를 위한 보안 실행 계층** — `.env`, 시크릿, 민감한 시스템 파일을 노출하지 않고 에이전트를 안전하게 통합하세요.

---

## 🔍 Secure-MCP란?

**Secure-MCP**는 MCP(Multi-Component Prompting) 또는 LLM 에이전트 시스템을 감싸는 보안 중심 미들웨어 프레임워크로 다음을 보장합니다:

- 🚫 `.env`, `API 키`, 시스템 파일, 개인 설정이 에이전트 로직에 **접근 불가능**합니다.
- ✅ MCP/에이전트 시스템이 보안 프록시를 통해 API 호출이나 토큰 검색 등의 **작업을 안전하게 수행**할 수 있습니다.
- 🧠 LLM 워크플로우, 에이전트 프레임워크(LangChain, AutoGen, CrewAI 등), 컨텍스트 기반 도구를 **보안을 해치지 않고** 지원합니다.

---

## 🧱 주요 기능

| 기능                           | 설명                                                                    |
|-------------------------------|-------------------------------------------------------------------------|
| 🔐 **SecureEnvBridge**         | 화이트리스트된 환경 변수만 접근 가능; `.env`는 직접 노출되지 않음            |
| 📂 **파일 접근 제어**            | `.env`, `secret.pem`, `key.json`, `config.yaml` 등의 파일 읽기 차단      |
| 📦 **보안 함수 프록시**          | 민감한 작업을 보안 호출 가능한 함수로 추상화                                |
| 📜 **감사 로깅**               | 민감한 리소스에 대한 모든 접근 시도를 기록                                  |
| 🧪 **샌드박스 실행**            | 선택적으로 격리된 환경(예: Docker, WASM)에서 MCP 코드 실행                 |
| ⚙️ **프레임워크 독립적**         | 모든 에이전트 시스템이나 LLM 파이프라인에 쉽게 연결                         |

---

## 🧰 사용 예시

```python
from secure_mcp.secure_env_bridge import secure_get, secure_open

# 화이트리스트된 환경 변수만 허용됨
api_key = secure_get("SERVICE_AUTH_TOKEN")  # ✅ 허용
db_pw = secure_get("DB_PASSWORD")           # ❌ 차단

# 안전한 파일 열기 (민감한 파일 차단)
with secure_open("safe_data.csv") as f:
    content = f.read()
```

안전성을 보장하기 위해 `os.getenv()`와 `open()` 대신 `SecureEnvBridge`를 사용하세요.

---

## 🔧 설치

```bash
git clone https://github.com/yourname/secure-mcp.git
cd secure-mcp
pip install -e .
```

내부 PyPI 배포를 위해 `setup.py` 또는 `pyproject.toml`로 패키징할 수도 있습니다.

---

## 🛠️ 아키텍처

```txt
[ 사용자 입력 / 에이전트 작업 ]
           ↓
[ SecureContextExecutor ]
           ↓
[ SecureEnvBridge / FileGuard ]
           ↓
[ 외부 API, 파일 또는 메모리 접근 ]
           ↓
[ LLM 에이전트 응답 ]
```

* MCP는 시크릿을 알 필요가 없습니다.
* SecureEnvBridge는 **볼트 인식 대리자**처럼 작동합니다.
* 모든 접근은 **제어되고, 로깅되며, 필터링**됩니다.

---

## 📄 예시 구조

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

## 🚧 로드맵

* [x] 화이트리스트 로더가 있는 SecureEnvBridge
* [x] 파일 접근 가드 (`open()` 패치)
* [ ] WASM 기반 실행 래퍼
* [ ] Docker화된 보안 MCP 실행기
* [ ] OpenAPI 프록시 어댑터
* [ ] LangChain / CrewAI용 에이전트 플러그인 시스템

---

## 🔐 라이선스

이 프로젝트는 **Apache License 2.0**에 따라 라이선스가 부여됩니다.
자세한 내용은 [LICENSE](./LICENSE) 파일을 참조하세요.

---

## 🤝 기여하기

풀 리퀘스트를 환영합니다.
주요 변경사항의 경우 먼저 이슈를 열어 변경하고자 하는 내용을 논의해 주세요.
자세한 지침은 `CONTRIBUTING.md`를 확인하세요.

---

## 📬 연락처

질문, 아이디어 또는 피드백이 있으신가요?
[이슈 열기](https://github.com/yourname/secure-mcp/issues) 또는 토론을 시작해 주세요.