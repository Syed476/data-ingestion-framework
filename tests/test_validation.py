import pandas as pd

from src.validation import (
    validate_columns,
    validate_duplicates
)


def test_required_columns_present():
    result = validate_columns(
        ["id", "name", "amount"],
        ["id", "name"]
    )

    assert result == []


def test_duplicate_detection():
    df = pd.DataFrame(
        {
            "id": [1, 1],
            "name": ["Ali", "Syed"]
        }
    )

    assert validate_duplicates(df, "id") is True