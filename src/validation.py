def validate_columns(columns, required_columns):
    missing_columns = []

    for column in required_columns:
        if column not in columns:
            missing_columns.append(column)

    return missing_columns


def validate_duplicates(df, primary_key):
    return bool(df[primary_key].duplicated().any())