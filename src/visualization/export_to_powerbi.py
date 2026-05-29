from pathlib import Path
import pandas as pd


def export_powerbi_tables(source_csv: str = "data/curated/healthcare_triage_dataset.csv", output_dir: str = "powerbi") -> list[str]:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(source_csv)
    outputs = []
    fact_path = Path(output_dir) / "fact_model_output.csv"
    df.to_csv(fact_path, index=False)
    outputs.append(str(fact_path))
    numeric = df.select_dtypes(include="number")
    kpi = numeric.mean(numeric_only=True).reset_index()
    kpi.columns = ["metric", "mean_value"]
    kpi_path = Path(output_dir) / "kpi_summary.csv"
    kpi.to_csv(kpi_path, index=False)
    outputs.append(str(kpi_path))
    return outputs


if __name__ == "__main__":
    print(export_powerbi_tables())
