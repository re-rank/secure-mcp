# 🛡️ Secure-MCP

> **LLM/MCPエージェント用セキュアな実行レイヤー** — `.env`、シークレット、機密システムファイルを公開せずにエージェントを安全に統合。

---

## 🔍 Secure-MCPとは？

**Secure-MCP**は、MCP（Multi-Component Prompting）またはLLMエージェントシステムをラップするセキュリティ重視のミドルウェアフレームワークで、以下を保証します：

- 🚫 `.env`、`APIキー`、システムファイル、プライベート設定がエージェントロジックから**アクセス不可能**。
- ✅ MCP/エージェントシステムは、セキュアプロキシ経由でAPIコールやトークン取得などの**操作を安全に実行**できます。
- 🧠 LLMワークフロー、エージェントフレームワーク（LangChain、AutoGen、CrewAIなど）、コンテキストベースツールを**セキュリティを損なうことなく**サポート。

---

## 🧱 主な機能

| 機能                           | 説明                                                                    |
|-------------------------------|-------------------------------------------------------------------------|
| 🔐 **SecureEnvBridge**         | ホワイトリスト化された環境変数のみアクセス可能；`.env`は直接公開されない        |
| 📂 **ファイルアクセス制御**       | `.env`、`secret.pem`、`key.json`、`config.yaml`などのファイル読み取りをブロック |
| 📦 **セキュア関数プロキシ**       | 機密操作をセキュアな呼び出し可能関数に抽象化                                 |
| 📜 **監査ログ**                | 機密リソースへのすべてのアクセス試行をログ記録                               |
| 🧪 **サンドボックス実行**        | オプションで隔離環境（例：Docker、WASM）でMCPコードを実行                    |
| ⚙️ **フレームワーク非依存**       | あらゆるエージェントシステムやLLMパイプラインに簡単にプラグイン                |

---

## 🧰 使用例

```python
from secure_mcp.secure_env_bridge import secure_get, secure_open

# ホワイトリスト化された環境変数のみ許可
api_key = secure_get("SERVICE_AUTH_TOKEN")  # ✅ 許可
db_pw = secure_get("DB_PASSWORD")           # ❌ ブロック

# 安全なファイルオープン（機密ファイルをブロック）
with secure_open("safe_data.csv") as f:
    content = f.read()
```

安全性を確保するために、`os.getenv()`と`open()`の代わりに`SecureEnvBridge`を使用してください。

---

## 🔧 インストール

```bash
git clone https://github.com/yourname/secure-mcp.git
cd secure-mcp
pip install -e .
```

内部PyPIデプロイメント用に`setup.py`または`pyproject.toml`でパッケージ化することもできます。

---

## 🛠️ アーキテクチャ

```txt
[ ユーザー入力 / エージェントタスク ]
           ↓
[ SecureContextExecutor ]
           ↓
[ SecureEnvBridge / FileGuard ]
           ↓
[ 外部API、ファイル、またはメモリアクセス ]
           ↓
[ LLMエージェントレスポンス ]
```

* MCPはシークレットを知る必要がありません。
* SecureEnvBridgeは**ボルト対応デリゲート**のように動作します。
* すべてのアクセスは**制御され、ログ記録され、フィルタリング**されます。

---

## 📄 構造例

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

## 🚧 ロードマップ

* [x] ホワイトリストローダー付きSecureEnvBridge
* [x] ファイルアクセスガード（`open()`パッチ）
* [ ] WASMベース実行ラッパー
* [ ] Docker化されたセキュアMCPランナー
* [ ] OpenAPIプロキシアダプター
* [ ] LangChain / CrewAI用エージェントプラグインシステム

---

## 🔐 ライセンス

このプロジェクトは**Apache License 2.0**の下でライセンスされています。
詳細は[LICENSE](./LICENSE)ファイルをご覧ください。

---

## 🤝 貢献

プルリクエストを歓迎します。
大きな変更の場合は、まず変更したい内容についてディスカッションするためにイシューを開いてください。
詳細な手順については`CONTRIBUTING.md`をご確認ください。

---

## 📬 お問い合わせ

質問、アイデア、フィードバックはありますか？
お気軽に[イシューを開く](https://github.com/yourname/secure-mcp/issues)か、ディスカッションを始めてください。