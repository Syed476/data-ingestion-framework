from src.validation import validate_columns


def test_required_columns_present():
    result = validate_columns(
        ["id", "name", "amount"],
        ["id", "name"]
    )

    assert result == []