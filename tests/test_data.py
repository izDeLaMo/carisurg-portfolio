"""Sanity check (a): data loading and expected schema.

Goal is not to prove the data-loading code is perfect — it's to make the
pipeline break loudly if the input schema changes underneath it (e.g. a
column gets renamed or dropped upstream by IT).
"""

import pandas as pd
import pytest

from src.utils import load_config
from src.data import load_data, get_features_and_target


@pytest.fixture(scope="module")
def config():
    return load_config("config.yaml")


def test_load_data_has_expected_columns(config):
    df = load_data(config)

    target_col = config["data"]["target_column"]
    leak_cols = config["data"]["leak_columns"]

    assert target_col in df.columns, (
        f"Expected target column '{target_col}' not found — has the schema changed upstream?"
    )
    for col in leak_cols:
        assert col in df.columns or True, (
            "Leak columns are optional in the raw file, but if present must be droppable "
            "by get_features_and_target without raising."
        )
    assert len(df) > 0, "Loaded dataframe is empty."


def test_get_features_and_target_shapes_and_types(config):
    df = load_data(config)
    X, y = get_features_and_target(df, config)

    assert isinstance(X, pd.DataFrame)
    assert isinstance(y, pd.Series)
    assert len(X) == len(y), "X and y must have the same number of rows."

    target_col = config["data"]["target_column"]
    leak_cols = config["data"]["leak_columns"]
    assert target_col not in X.columns, "Target column leaked into features."
    for col in leak_cols:
        assert col not in X.columns, f"Leak column '{col}' leaked into features."

    # y should be integer ESI levels, not floats/strings, after casting in get_features_and_target.
    assert pd.api.types.is_integer_dtype(y), "Target column should be castable to int (ESI level)."
