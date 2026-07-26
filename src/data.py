"""Data loading and cleaning.

Logic is unchanged from the Week 6/7 notebooks — only restructured into
functions so it can be imported instead of copy-pasted between notebooks.
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(config: dict) -> pd.DataFrame:
    """Load the cleaned triage dataset.

    Resolves the path from config first; falls back to the Colab/Drive path
    used during development if the repo-relative path isn't found (keeps
    notebooks that still run in Colab working without edits).
    """
    repo_relative_path = config["data"]["path"]
    colab_fallback_path = "/content/drive/MyDrive/Colab Notebooks/Carisurg/data/triage_clean_interim.csv"

    data_path = repo_relative_path if os.path.exists(repo_relative_path) else colab_fallback_path

    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Could not find dataset at '{repo_relative_path}' or the Colab fallback path. "
            "Check config.yaml -> data.path, or governance access to the data store."
        )

    df = pd.read_csv(data_path)
    return df


def get_features_and_target(df: pd.DataFrame, config: dict) -> tuple[pd.DataFrame, pd.Series]:
    """Split the raw dataframe into X, y and drop outcome-leaking columns.

    Leak columns (disposition, previousdispo) are recorded at/after the
    triage decision itself, so including them would let the model see the
    answer. Feature scope is numeric + already-binary cc_* flags, matching
    Week 6/7 exactly.
    """
    target_col = config["data"]["target_column"]
    leak_cols = config["data"]["leak_columns"]

    X = df.drop(columns=[target_col] + [c for c in leak_cols if c in df.columns])
    y = df[target_col].astype(int)

    # Numeric + already-binary cc_* features only (same scope as Week 6/7).
    X = X.select_dtypes(include=np.number)

    return X, y


def split_data(X: pd.DataFrame, y: pd.Series, config: dict):
    """Stratified train/test split using the seed pinned in config.yaml.

    Using the same seed and split logic across model comparisons is what
    makes the model-selection table in docs/ a fair comparison — every
    model is evaluated on exactly the same unseen patients.
    """
    test_size = config["data"]["test_size"]
    stratify_arg = y if config["data"]["stratify"] else None
    seed = config["seed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        stratify=stratify_arg,
        random_state=seed,
    )
    return X_train, X_test, y_train, y_test
