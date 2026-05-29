# Deployment Steps

1. Create Azure App Service with Python runtime.
2. Push repository to GitHub.
3. Add App Service deployment using Deployment Center or GitHub Actions.
4. Add environment variables from `.env.example` into Azure App Settings.
5. Confirm `/health`, `/docs`, `/api/v1/status`, and `/api/v1/agents/ask`.
6. Capture proof screenshots for project documentation.

Technical walkthrough line: *I deployed Intelligent Healthcare Support System as a FastAPI service on Azure App Service, connected it to Azure OpenAI using environment variables, and kept local fallback to avoid demo failure when keys are unavailable.*
