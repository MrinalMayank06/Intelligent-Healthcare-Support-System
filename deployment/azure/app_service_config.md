# Azure App Service Configuration

Runtime stack: Python 3.12  
Startup command:

```bash
gunicorn -w 2 -k uvicorn.workers.UvicornWorker src.api.main:app
```

Required App Settings:
- `MONGODB_URI`
- `MONGODB_DB=healthcare_support_db`
- `USE_AZURE_OPENAI=true` after keys are configured
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_API_VERSION`

Security: never commit keys. Use App Service Configuration or Key Vault references.
