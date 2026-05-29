# API Reference - Intelligent Healthcare Support System

| Endpoint | Method | Purpose |
|---|---:|---|
| `/health` | GET | Runtime health check |
| `/api/v1/status` | GET | Project and component status |
| `/api/v1/data/ingest` | POST | Stores one raw business record |
| `/api/v1/data/recent` | GET | Reads latest ingested records |
| `/api/v1/ml/predict` | POST | Runs persisted ML model inference |
| `/api/v1/documents/search` | POST | Searches the local knowledge base through RAG flow |
| `/api/v1/agents/ask` | POST | Routes a user question through MCP-style orchestration |
| `/api/v1/agents/domain-advice` | POST | Combines domain model output with agent explanation |
| `/api/v1/analytics/kpis` | GET | Generates KPI summary for dashboard layer |
| `/api/v1/mcp/trace` | GET | Returns recent orchestration trace |
| `/api/v1/logs/agents` | GET | Reads recent agent logs |
| `/api/v1/logs/predictions` | GET | Reads recent prediction logs |

## Typical use order

1. Run `/health` to confirm the app is running.
2. Run `/api/v1/status` to confirm project metadata.
3. Use `/api/v1/ml/predict` for model prediction.
4. Use `/api/v1/documents/search` for knowledge retrieval.
5. Use `/api/v1/agents/ask` for orchestrated agent response.
6. Use `/api/v1/analytics/kpis` for dashboard summary.
