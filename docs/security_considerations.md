# Security Considerations

- Secrets are kept in `.env` locally and Azure App Settings/Key Vault in cloud.
- API validates request bodies using Pydantic schemas.
- Global exception handlers prevent stack traces from leaking to users.
- Agent output includes retrieved context and trace for observability.
- In healthcare/finance style domains, the assistant must be treated as decision support, not final authority.
- Database connection string is not hardcoded.
