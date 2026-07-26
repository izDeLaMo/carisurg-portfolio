"""Sanity check (b): training smoke test on a small synthetic slice (~50 rows).

Goal: prove the full pipeline (build -> scale -> train -> predict -> evaluate)
runs end to end without crashing, fast, without depending on the real
(potentially large or access-controlled) dataset. This is not a check on
model quality — a real accuracy/recall check belongs in the model-selection
table, not here.
"""

import numpy as np
import pandas as pd

from src.utils import load_config
from src.features import scale_features
from src.model import build_model, train_and_predict, evaluate


def _make_synthetic_frame(n_rows: int = 50, n_features: int = 6, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    X = pd.DataFrame(
        rng.normal(size=(n_rows, n_features)),
        columns=[f"feature_{i}" for i in range(n_features)],
    )
    # 5 ESI-like classes (1-5), imbalanced on purpose like the real target.
    y = pd.Series(rng.choice([1, 2, 3, 4, 5], size=n_rows, p=[0.05, 0.15, 0.3, 0.3, 0.2]), name="esi")
    return X, y


def test_pipeline_smoke_runs_on_small_slice():
    config = load_config("config.yaml")

    X, y = _make_synthetic_frame(n_rows=50)

    # Small manual split instead of src.data.split_data, since stratified splitting
    # on 50 rows with 5 classes can fail on the smallest class — the point here is
    # "does the pipeline run", not "is this a representative split".
    split_point = 40
    X_train, X_test = X.iloc[:split_point], X.iloc[split_point:]
    y_train, y_test = y.iloc[:split_point], y.iloc[split_point:]

    X_train_final, X_test_final, _ = scale_features(X_train, X_test, config)

    model = build_model(config)
    y_pred, train_time, inference_time = train_and_predict(model, X_train_final, y_train, X_test_final)

    assert len(y_pred) == len(y_test), "Prediction count must match test set size."
    assert train_time >= 0
    assert inference_time >= 0

    results = evaluate(y_test, y_pred, config)
    assert "accuracy" in results
    assert 0.0 <= results["accuracy"] <= 1.0
