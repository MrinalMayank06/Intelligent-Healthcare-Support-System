# Start Here - Intelligent Healthcare Support System

## 1. Install

```bash
pip install -r requirements.txt
```

## 2. Train model

```bash
python scripts/run_training.py
```

## 3. Build knowledge embeddings

```bash
python scripts/build_chroma_store.py
```

## 4. Run API

```bash
python scripts/run_api.py
```

## 5. Open API docs

```text
http://127.0.0.1:8000/docs
```

## 6. Main files to open first

1. `README.md`
2. `src/api/main.py`
3. `src/api/routes/ml_routes.py`
4. `src/ml/training/train_model.py`
5. `src/agents/mcp/mcp_orchestrator.py`
6. `docs/implementation_deep_dive.md`
