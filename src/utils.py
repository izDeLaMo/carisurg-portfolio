"""Shared helpers: config loading and timing utilities.

Kept deliberately small — this module has no project-specific logic in it,
only plumbing that data.py, features.py, and model.py all need.
"""

import time
import yaml


def load_config(config_path: str = "config.yaml") -> dict:
    """Load the single YAML config that drives training.

    All paths, hyperparameters, and the pinned model choice live here so
    nothing project-specific is hardcoded inside src/.
    """
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config


def time_fit_predict(model, X_train, y_train, X_test):
    """Fit a model, predict on X_test, and return predictions plus timing.

    Returns
    -------
    y_pred : array-like
    train_time : float (seconds)
    inference_time_per_pred : float (seconds per prediction)
    """
    t0 = time.perf_counter()
    model.fit(X_train, y_train)
    train_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    y_pred = model.predict(X_test)
    inference_time_total = time.perf_counter() - t0
    inference_time_per_pred = inference_time_total / len(X_test)

    return y_pred, train_time, inference_time_per_pred
