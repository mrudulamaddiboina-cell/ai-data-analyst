import pandas as pd


def analyze_dataset(file_path):
    """
    Analyze a CSV dataset and return basic information.
    """

    df = pd.read_csv(file_path)

    analysis = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict()
    }

    return analysis
