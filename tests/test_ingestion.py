from src.ingestion import ingest


def test_ingestion():
    result = ingest(
        "data/sample_input.csv",
        "config/validation_rules.json"
    )

    assert len(result) > 0