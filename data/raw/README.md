# Raw Data Zone

This folder simulates the raw landing zone in a data engineering pipeline.

Raw -> Staged -> Curated idea:
- Raw: original CSV/API records
- Staged: cleaned and standardized data
- Curated: ML/Power BI-ready table `healthcare_triage_dataset.csv`

In Azure, this can map to ADF ingestion + Fabric Lakehouse or Databricks Delta tables.
