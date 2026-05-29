# Implementation Deep Dive - Intelligent Healthcare Support System

## 1. Backend design

The backend starts from `src/api/main.py`. This file creates the FastAPI object, includes route modules, and exposes basic health/status endpoints. All business routes are kept in `src/api/routes/` so the application remains easy to maintain.

## 2. Request validation

`src/api/schemas/request_models.py` contains Pydantic models. The prediction request has strongly typed fields for the selected domain. This avoids invalid payloads entering the ML layer.

## 3. Data storage

`src/database/mongo_client.py` tries to connect to MongoDB or Cosmos DB Mongo API. If the database is unavailable, `src/database/crud.py` stores data in memory. This allows the project to run in local mode and cloud mode with the same code.

## 4. ML training

The training pipeline follows a normal production-style sequence:

```text
load raw data -> clean data -> feature engineering -> train/test split -> model training -> metrics -> joblib persistence
```

The selected target is `triage_level`. The selected model is `RandomForestClassifier for triage-level classification`. The model is saved inside `artifacts/models/`, and metrics are saved inside `artifacts/metrics/`.

## 5. ML inference

`src/ml/inference/predict.py` loads the saved joblib pipeline. The pipeline contains preprocessing and model steps together, so API inference uses the same transformations that were used during training.

## 6. RAG layer

The knowledge base is stored in `artifacts/knowledge/knowledge_base.csv`. `scripts/build_chroma_store.py` creates lightweight local embeddings in JSON format. The retrieval code is deliberately simple, readable and reproducible.

## 7. Agent orchestration

`src/agents/mcp/mcp_orchestrator.py` performs intent routing. Analytics questions go to `AnalyticsAgent`. Knowledge or policy questions go to the RAG pipeline. Each call stores a trace that can be viewed from `/api/v1/mcp/trace`.

## 8. Domain agent

`src/agents/triage_agent/agent.py` is the project-specific agent. It calls the ML model, prepares context, and uses `LLMClient` to generate an explanation. With environment variables, it can call Azure OpenAI. Without keys, it produces a deterministic local fallback response.

## 9. Analytics flow

The analytics layer reads curated CSV files and returns numeric KPI summaries. Power BI can import curated tables and generated KPI CSV files.

## 10. Deployment flow

The same FastAPI app can be deployed on Azure App Service. Environment variables control database and Azure OpenAI connectivity. CI/CD template is provided in `deployment/ci_cd/github_actions.yml`.

## 11. Data files included

- `data/raw/patient_encounters.csv`: compact training dataset
- `data/raw/high_volume_patient_events.csv`: high-volume operational events
- `data/staged/patient_staged_features.csv`: staged features
- `data/curated/healthcare_triage_dataset.csv`: model-ready table
- `data/curated/patient_dashboard_facts.csv`: dashboard-ready facts
- `artifacts/monitoring/agent_model_request_log.jsonl`: observability log
