import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def safe_mkdir(path: str) -> None:
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def main() -> None:
    train_path = "train.csv"
    test_path = "test.csv"
    out_dir = "outputs"
    safe_mkdir(out_dir)

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    print(f"train_shape={train_df.shape} test_shape={test_df.shape}")

    # Basic missing value report.
    missing = train_df.isna().sum().sort_values(ascending=False)
    top_missing = missing[missing > 0].head(10)
    if len(top_missing) > 0:
        print("top_missing_columns:")
        print(top_missing)
    else:
        print("no_missing_values_in_train")

    # Split features/label.
    y = train_df["win"].astype("int8")
    X = train_df.drop(columns=["win"])
    if "id" in X.columns:
        X = X.drop(columns=["id"])
    if "id" in test_df.columns:
        test_df = test_df.drop(columns=["id"])

    # Simple preprocessing: fill missing values with train median.
    numeric_cols = X.select_dtypes(include=[np.number]).columns
    medians = X[numeric_cols].median()
    X[numeric_cols] = X[numeric_cols].fillna(medians)
    test_df[numeric_cols] = test_df[numeric_cols].fillna(medians)

    # Save processed data for reuse.
    X.to_csv(os.path.join(out_dir, "train_processed.csv"), index=False)
    test_df.to_csv(os.path.join(out_dir, "test_processed.csv"), index=False)

    # Sample for visualization to keep plots fast.
    sample_n = min(200_000, len(X))
    sample_idx = np.random.RandomState(42).choice(len(X), size=sample_n, replace=False)
    X_sample = X.iloc[sample_idx]
    y_sample = y.iloc[sample_idx]

    # 1) Label distribution.
    plt.figure(figsize=(5, 4))
    counts = y.value_counts().sort_index()
    plt.bar(counts.index.astype(str), counts.values)
    plt.title("Label distribution (win)")
    plt.xlabel("win")
    plt.ylabel("count")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "label_distribution.png"), dpi=150)
    plt.close()

    # 2) Histograms for key features if present.
    key_cols = ["kills", "deaths", "assists", "totdmgdealt", "totdmgtaken"]
    present_cols = [c for c in key_cols if c in X_sample.columns]
    if present_cols:
        n = len(present_cols)
        rows = 2
        cols = int(np.ceil(n / rows))
        plt.figure(figsize=(4 * cols, 3.5 * rows))
        for i, col in enumerate(present_cols, start=1):
            plt.subplot(rows, cols, i)
            plt.hist(X_sample[col], bins=50, color="#2a9d8f", alpha=0.8)
            plt.title(col)
            plt.xlabel("value")
            plt.ylabel("count")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "feature_histograms.png"), dpi=150)
        plt.close()

    # 3) Correlation heatmap for top correlated features with label.
    corr_with_label = X_sample[numeric_cols].corrwith(y_sample).abs().sort_values(ascending=False)
    top_cols = corr_with_label.head(12).index.tolist()
    corr_mat = X_sample[top_cols].corr()
    plt.figure(figsize=(7, 6))
    plt.imshow(corr_mat, cmap="coolwarm", vmin=-1, vmax=1)
    plt.xticks(range(len(top_cols)), top_cols, rotation=60, ha="right")
    plt.yticks(range(len(top_cols)), top_cols)
    plt.colorbar(label="correlation")
    plt.title("Top feature correlations")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "top_feature_correlation.png"), dpi=150)
    plt.close()

    # 4) If submission exists, show prediction distribution.
    submission_path = "submission.csv"
    if os.path.isfile(submission_path):
        sub = pd.read_csv(submission_path)
        if "win" in sub.columns:
            plt.figure(figsize=(5, 4))
            sub_counts = sub["win"].value_counts().sort_index()
            plt.bar(sub_counts.index.astype(str), sub_counts.values, color="#264653")
            plt.title("Submission prediction distribution")
            plt.xlabel("win")
            plt.ylabel("count")
            plt.tight_layout()
            plt.savefig(os.path.join(out_dir, "submission_distribution.png"), dpi=150)
            plt.close()

    print(f"saved outputs to {out_dir}\\")


if __name__ == "__main__":
    main()
