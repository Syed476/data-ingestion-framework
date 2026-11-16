import pandas as pd

from src.config_loader import load_rules
from src.validation import (
    validate_columns,
    validate_duplicates
)


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

    if rules["check_duplicates"]:
        has_duplicates = validate_duplicates(
            df,
            rules["primary_key"]
        )

        if has_duplicates:
            raise ValueError(
                "Duplicate records detected"
            )

    return df