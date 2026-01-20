import os

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from xgboost import XGBClassifier


def main() -> None:
    # Update these paths if your CSV files are elsewhere.
    train_path = "train.csv"
    test_path = "test.csv"

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    # Split features/label.
    y = train_df["win"].astype("int8")
    X = train_df.drop(columns=["win"])
    X_test = test_df.drop(columns=["id"])

    # Drop id from training features too if present.
    if "id" in X.columns:
        X = X.drop(columns=["id"])

    # Use a subset for tuning to keep it fast on big data.
    tune_rows = 200_000
    if len(X) > tune_rows:
        tune_df = train_df.sample(n=tune_rows, random_state=42)
        y_tune = tune_df["win"].astype("int8")
        X_tune = tune_df.drop(columns=["win"])
        if "id" in X_tune.columns:
            X_tune = X_tune.drop(columns=["id"])
    else:
        X_tune = X
        y_tune = y

    # Quick parameter search.
    param_grid = [
        {
            "n_estimators": 500,
            "max_depth": 6,
            "learning_rate": 0.08,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
        },
        {
            "n_estimators": 600,
            "max_depth": 5,
            "learning_rate": 0.07,
            "subsample": 0.9,
            "colsample_bytree": 0.9,
        },
    ]

    skf = StratifiedKFold(n_splits=2, shuffle=True, random_state=42)
    best_score = -1.0
    best_params = None

    for params in param_grid:
        fold_scores = []
        for train_idx, valid_idx in skf.split(X_tune, y_tune):
            X_train = X_tune.iloc[train_idx]
            y_train = y_tune.iloc[train_idx]
            X_valid = X_tune.iloc[valid_idx]
            y_valid = y_tune.iloc[valid_idx]

            model = XGBClassifier(
                tree_method="hist",
                eval_metric="logloss",
                n_jobs=-1,
                **params,
            )
            model.fit(
                X_train,
                y_train,
                eval_set=[(X_valid, y_valid)],
                verbose=False,
            )
            valid_pred = model.predict(X_valid)
            fold_scores.append(accuracy_score(y_valid, valid_pred))

        avg_score = sum(fold_scores) / len(fold_scores)
        print(f"cv_accuracy={avg_score:.6f} params={params}")
        if avg_score > best_score:
            best_score = avg_score
            best_params = params

    print(f"best_cv_accuracy={best_score:.6f} params={best_params}")

    # Fit on full data using the best params.
    model = XGBClassifier(
        tree_method="hist",
        eval_metric="logloss",
        n_jobs=-1,
        **best_params,
    )
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.1, random_state=42, stratify=y
    )
    model.fit(
        X_train,
        y_train,
        eval_set=[(X_train, y_train), (X_valid, y_valid)],
        verbose=False,
    )

    # Save loss curve.
    evals = model.evals_result()
    if evals:
        out_dir = "outputs"
        os.makedirs(out_dir, exist_ok=True)
        train_loss = evals.get("validation_0", {}).get("logloss", [])
        valid_loss = evals.get("validation_1", {}).get("logloss", [])
        if train_loss and valid_loss:
            plt.figure(figsize=(6, 4))
            plt.plot(train_loss, label="train")
            plt.plot(valid_loss, label="valid")
            plt.title("Logloss curve")
            plt.xlabel("iteration")
            plt.ylabel("logloss")
            plt.legend()
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "loss_curve.png"), dpi=150)
            plt.close()

    test_pred = model.predict(X_test)
    submission = pd.DataFrame({"win": test_pred})
    submission.to_csv("submission.csv", index=False, encoding="utf-8")
    print("saved submission.csv (win-only, utf-8)")


if __name__ == "__main__":
    main()
