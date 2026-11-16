import pandas as pd

from src.config_loader import load_rules
from src.validation import validate_columns


def ingest(file_path, config_path):
    df = pd.read_csv(file_path)

    rules = load_rules(config_path)

    missing_columns = validate_columns(
        df.columns.tolist(),
        rules["required_columns"]
    )

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return df