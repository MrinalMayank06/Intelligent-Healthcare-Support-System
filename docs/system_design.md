# System Design - Intelligent Healthcare Support System

## Objective
This platform supports patient symptom triage, medical information retrieval, and patient analytics. It is designed as decision support only, not a replacement for doctors.

## Main layers
1. **FastAPI backend** exposes APIs for ingestion, prediction, document search, analytics and agent interaction.
2. **Data layer** stores raw domain records in MongoDB/Cosmos DB and CSV files for reproducible local demo.
3. **ML layer** cleans data, creates features, trains `RandomForestClassifier for symptom triage`, persists model as `artifacts/models/triage_model.joblib`.
4. **GenAI layer** contains RAG + agents + MCP-style orchestrator.
5. **Azure layer** deploys API on App Service and optionally connects Azure OpenAI, Azure AI Search, Cosmos DB, Fabric/ADF.
6. **Analytics layer** exports curated tables to Power BI.

## Request lifecycle
User -> FastAPI route -> schema validation -> service/agent/model -> database/logging -> formatted response.

## Why this architecture
It separates API, ML, RAG, database and deployment concerns. This makes the project easy to explain in technical walkthrough and easy to extend later.
