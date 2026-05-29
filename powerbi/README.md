# Power BI Dashboard Plan - Intelligent Healthcare Support System

Import these generated CSV files into Power BI:
- `data/curated/healthcare_triage_dataset.csv` as fact table
- `powerbi/kpi_summary.csv` after running `python src/visualization/export_to_powerbi.py`

Suggested pages:
1. Executive Overview: total records, prediction distribution, high-risk count.
2. Model Output: target distribution and confidence/probability indicators.
3. Trends & Alerts: anomaly/risk trend by category/time/shift.
4. Agent Insights: show common questions and retrieved document topics.

Publish/share proof can be screenshots from Power BI Service.
