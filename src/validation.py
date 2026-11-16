def validate_columns(columns, required_columns):
    missing_columns = []

    for column in required_columns:
        if column not in columns:
            missing_columns.append(column)

    return missing_columns