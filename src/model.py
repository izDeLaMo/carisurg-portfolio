"""Model construction, training, and evaluation.

Only the model named in config.yaml (model.name) is built by build_model().
Random Forest / Decision Tree are supported here too so the comparison
models behind docs/model-selection.md can be regenerated later if needed,
but scripts/train.py only ever trains the pinned model by default.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)

from src.utils import time_fit_predict

_MODEL_REGISTRY = {
    "logistic_regression": LogisticRegression,
    "decision_tree": DecisionTreeClassifier,
    "random_forest": RandomForestClassifier,
    "stratified_random": DummyClassifier,
}


def build_model(config: dict):
    """Instantiate the model named in config.yaml with its pinned hyperparameters."""
    model_name = config["model"]["name"]
    if model_name not in _MODEL_REGISTRY:
        raise ValueError(
            f"Unknown model '{model_name}' in config.yaml. "
            f"Supported: {list(_MODEL_REGISTRY.keys())}"
        )
    hyperparameters = config["model"]["hyperparameters"]
    return _MODEL_REGISTRY[model_name](**hyperparameters)


def train_and_predict(model, X_train, y_train, X_test):
    """Fit the model and return predictions plus train/inference timing."""
    return time_fit_predict(model, X_train, y_train, X_test)


def evaluate(y_test, y_pred, config: dict) -> dict:
    """Compute the standard metric set plus the ESI Level 1 recall override.

    Macro (not weighted) precision/recall/F1 are used throughout because
    ESI Level 1 is rare, and averaging by class support would let a model
    look strong overall while still failing that class specifically.
    """
    results = {
        "accuracy": accuracy_score(y_test, y_pred),
        "macro_precision": precision_score(y_test, y_pred, average="macro", zero_division=0),
        "macro_recall": recall_score(y_test, y_pred, average="macro", zero_division=0),
        "macro_f1": f1_score(y_test, y_pred, average="macro"),
    }

    critical = config.get("evaluation", {}).get("critical_class_recall")
    if critical:
        report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
        class_label = str(critical["class_label"])
        results[critical["metric_name"]] = report.get(class_label, {}).get("recall", float("nan"))

    return results
