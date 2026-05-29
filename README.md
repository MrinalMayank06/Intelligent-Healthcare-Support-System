# Intelligent Healthcare Support System

## Overview

A healthcare decision-support platform for symptom triage, medical information retrieval, and patient analytics.

The solution is built as an end-to-end **Multi-Agent AI Platform with GenAI, Analytics, Data Engineering flow and Azure-ready deployment**. It uses a modular Python backend, a persisted machine learning model, a lightweight Retrieval-Augmented Generation pipeline, a domain-specific agent, analytics exports for Power BI, and cloud deployment configuration.

## Domain scope

**Selected domain:** Healthcare  
**Problem statement:** Symptom triage + medical information assistant + patient data analytics  
**Primary dataset:** patient encounters with symptoms, vitals, age, chronic-condition flag and triage label  
**ML target:** `triage_level`  
**Main model:** RandomForestClassifier for triage-level classification  
**Main domain agent:** `TriageAgent`

## How this project is different from Smart Retail

This project follows the same engineering pattern as the Smart Retail platform, but every business layer is changed for the selected domain.

| Layer | Smart Retail pattern | This project pattern |
|---|---|---|
| Business use case | Demand, anomaly, product support | Symptom triage + medical information assistant + patient data analytics |
| Input data | sales/orders/products/customers | patient encounters with symptoms, vitals, age, chronic-condition flag and triage label |
| ML target | demand or anomaly output | `triage_level` |
| Domain agent | sales/support agent | `TriageAgent` |
| RAG content | retail/product knowledge | domain knowledge for Healthcare |
| Dashboard | demand, sales, anomaly, customers | Triage distribution, High-risk symptom groups, Oxygen and heart-rate trend |
| Cloud setup | App Service + Azure OpenAI + data services | same cloud architecture with Healthcare data and KPIs |

## Repository structure

```text
Intelligent-Healthcare-Support-System/
├── artifacts/
│   ├── knowledge/              # CSV knowledge base + lightweight embeddings
│   ├── metrics/                # model training metrics
│   ├── models/                 # persisted joblib models
│   └── monitoring/             # generated operational request logs
├── configs/                    # project-level YAML config
├── data/
│   ├── raw/                    # raw landing-zone files
│   ├── staged/                 # staged feature tables
│   └── curated/                # ML/Power BI-ready facts
├── deployment/
│   ├── azure/                  # App Service, keys, model deployment notes
│   └── ci_cd/                  # GitHub Actions YAML template
├── docs/                       # architecture, API, RAG, MCP and deployment diagrams
├── powerbi/                    # dashboard plan and exported CSV files
├── scripts/                    # run API, retrain model, build knowledge store
├── src/
│   ├── agents/                 # RAG, analytics, MCP-style orchestration, domain agent
│   ├── api/                    # FastAPI app, routes, schemas, middleware
│   ├── common/                 # settings, logger, constants, exceptions
│   ├── database/               # MongoDB/Cosmos DB access with memory fallback
│   ├── ml/                     # data pipeline, model training and inference
│   ├── services/               # clean application service layer
│   └── visualization/          # Power BI export helper
├── tests/                      # pytest checks
├── README.md
├── START_HERE.md
└── requirements.txt
```

## Component mapping

### A. Python full-stack backend

The backend is implemented with **FastAPI**. It exposes ingestion, prediction, document search, agent, analytics and log endpoints. Request validation is handled through Pydantic models in `src/api/schemas/request_models.py`.

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

### B. Machine learning layer

The ML pipeline is placed under `src/ml/`.

| File | Responsibility |
|---|---|
| `data_pipeline/loader.py` | Loads raw CSV data from the raw zone |
| `data_pipeline/preprocessing.py` | Cleans missing values and duplicate rows |
| `data_pipeline/feature_engineering.py` | Adds simple domain-specific derived features |
| `training/train_model.py` | Trains and persists the sklearn model |
| `inference/predict.py` | Loads the joblib model and predicts for API payloads |

Model details:
- Target column: `triage_level`
- Input features: `age`, `primary_symptom`, `fever`, `oxygen_saturation`, `heart_rate`, `pain_level`, `symptom_days`, `chronic_condition`
- Persisted model: `artifacts/models/`
- Metrics: `artifacts/metrics/training_metrics.json`

### C. GenAI, RAG and agents

The GenAI layer is intentionally modular:

| Component | File | Role |
|---|---|---|
| Domain agent | `src/agents/triage_agent/agent.py` | Combines ML prediction with domain-specific explanation |
| RAG pipeline | `src/agents/support_agent/rag_pipeline.py` | Retrieves knowledge snippets and creates grounded answers |
| Vector store | `src/agents/support_agent/vector_store.py` | Lightweight token-based local retrieval for reproducible demo |
| Analytics agent | `src/agents/analytics_agent/agent.py` | Reads curated facts and returns KPI summaries |
| MCP-style orchestrator | `src/agents/mcp/mcp_orchestrator.py` | Selects the right tool and stores trace |
| LLM wrapper | `src/agents/shared/llm_client.py` | Uses Azure OpenAI when configured, otherwise local fallback |

Sample knowledge question:
```text
What action should be taken when oxygen saturation is low and breathing issue is reported?
```

### D. Azure AI and cloud readiness

The project includes cloud configuration for:
- Azure App Service
- Azure OpenAI / Azure AI Foundry
- Cosmos DB Mongo API
- Azure AI Search optional
- Fabric/ADF style pipeline

Secrets are not hardcoded. Local values can be placed in `.env`; cloud values should be configured through Azure App Service Configuration or Key Vault references.

### E. Data engineering flow

The repository contains a local version of the data engineering flow:

```text
Raw zone -> Staged zone -> Curated zone -> ML training/inference -> Power BI dashboard
```

| Zone | Folder | Meaning |
|---|---|---|
| Raw | `data/raw/` | original landing-zone data and high-volume operational events |
| Staged | `data/staged/` | cleaned/standardized feature-level data |
| Curated | `data/curated/` | business facts ready for ML and dashboarding |

On Azure, this maps to ADF/Fabric/Databricks pipelines with Delta/parquet-style storage.

### F. Analytics and Power BI

Power BI can import:
- `data/curated/healthcare_triage_dataset.csv`
- `data/curated/patient_dashboard_facts.csv`
- `powerbi/fact_model_output.csv`
- `powerbi/kpi_summary.csv`

Dashboard pages:
- Triage distribution
- High-risk symptom groups
- Oxygen and heart-rate trend
- Age-band risk
- Agent support logs

### G. Deployment

The FastAPI app is deployable on Azure App Service. The suggested startup command is documented in `deployment/azure/app_service_config.md`.

```bash
gunicorn -w 2 -k uvicorn.workers.UvicornWorker src.api.main:app
```

## Local setup

```bash
cd Intelligent-Healthcare-Support-System
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/run_training.py
python scripts/build_chroma_store.py
python scripts/run_api.py
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

## Sample prediction request

Use `/api/v1/ml/predict` in Swagger. The schema already contains a domain-specific sample payload.

## Code flow

```text
Client request
  -> FastAPI route
  -> Pydantic validation
  -> service/model/agent call
  -> database or memory fallback logging
  -> formatted JSON response
```

For prediction:

```text
POST /api/v1/ml/predict
  -> PredictionRequest schema
  -> src/ml/inference/predict.py
  -> artifacts/models/*.joblib
  -> prediction log
  -> response
```

For agent search:

```text
POST /api/v1/agents/ask
  -> MCPOrchestrator
  -> intent detection
  -> RAGPipeline or AnalyticsAgent
  -> trace
  -> response
```

## Quality notes

- Code is separated into API, services, ML, agents, database and visualization layers.
- The application can run locally even without MongoDB because `src/database/crud.py` has memory fallback.
- Azure OpenAI is optional during local execution because `src/agents/shared/llm_client.py` has fallback response mode.
- Tests are included in `tests/test_api.py`.
- Generated large datasets are included to support analytics, data engineering and Power BI demonstrations.
