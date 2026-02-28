import re


def validate_data(df, rules):
    failures = {}
    total_rows = int(len(df))  # convert to python int

    for rule in rules:
        col = rule.get("column")

        if col not in df.columns:
            continue

        if rule["rule"] == "not_null":
            failures[col] = int(df[col].isnull().sum())

        if rule["rule"] == "between":
            failures[col] = int(
                (
                    (df[col] < rule["min"]) |
                    (df[col] > rule["max"])
                ).sum()
            )

        if rule["rule"] == "regex" and rule.get("pattern") == "email":
            pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            failures[col] = int(
                (~df[col].astype(str).str.match(pattern)).sum()
            )

        if rule["rule"] == "greater_than":
            failures[col] = int((df[col] < rule["min"]).sum())

    return {
        "total_rows": total_rows,
        "failed_rows": int(sum(failures.values())),
        "column_failures": failures
    }