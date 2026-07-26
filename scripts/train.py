"""Entry point: train the pinned model from config.yaml.

Usage:
    python scripts/train.py --config config.yaml

This is the ONE way the final model is trained. It reads config.yaml,
loads and splits the data, builds the pinned model (Logistic Regression),
scales features if the model needs it, trains, evaluates, and prints the
results. No hyperparameters or paths live in this file — they all come
from config.yaml so the run is reproducible from that one file alone.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse
import sys

from src.utils import load_config
from src.data import load_data, get_features_and_target, split_data
from src.features import scale_features
from src.model import build_model, train_and_predict, evaluate


def main():
    parser = argparse.ArgumentParser(description="Train the pinned Phase 3 model.")
    parser.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)

    print(f"Loading data per config: {config['data']['path']}")
    df = load_data(config)

    X, y = get_features_and_target(df, config)
    print(f"Feature count: {X.shape[1]}")
    print("Target distribution:")
    print(y.value_counts().sort_index())

    X_train, X_test, y_train, y_test = split_data(X, y, config)
    print(f"Train: {X_train.shape}  Test: {X_test.shape}")

    X_train_final, X_test_final, _ = scale_features(X_train, X_test, config)

    model = build_model(config)
    print(f"Training pinned model: {config['model']['name']}")
    y_pred, train_time, inference_time = train_and_predict(model, X_train_final, y_train, X_test_final)

    results = evaluate(y_test, y_pred, config)

    print("\n--- Results ---")
    for metric, value in results.items():
        print(f"{metric}: {value:.4f}")
    print(f"train_time_s: {train_time:.4f}")
    print(f"inference_time_s_per_pred: {inference_time:.8f}")


if __name__ == "__main__":
    sys.exit(main())
