"""Feature engineering.

The pinned model (Logistic Regression) needs scaled features; the
tree-based comparison models used in Weeks 6-7 did not. Scaling is
therefore config-driven (model.scale_features) rather than hardcoded,
so this module stays correct if the pinned model ever changes.
"""

from sklearn.preprocessing import StandardScaler


def scale_features(X_train, X_test, config: dict):
    """Fit a StandardScaler on X_train and apply it to X_train/X_test.

    Returns the scaled arrays and the fitted scaler (so it can be reused
    at inference time on new patients, not just on the held-out test set).
    """
    if not config["model"].get("scale_features", False):
        return X_train, X_test, None

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler
