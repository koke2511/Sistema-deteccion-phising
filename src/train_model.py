import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

from features import extract_features


def load_urls_dataset(file_path: str) -> pd.DataFrame:
    rows = []

    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        next(file)

        for line_number, line in enumerate(file, start=2):
            line = line.strip()

            if not line:
                continue

            try:
                url, label, source = line.rsplit(",", 2)

                rows.append(
                    {
                        "url": url,
                        "label": int(label),
                        "source": source,
                    }
                )

            except ValueError:
                print(f"Línea ignorada por formato incorrecto: {line_number}")

    return pd.DataFrame(rows)


def evaluate_model(model_name: str, model, X_test, y_test):
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"\n=== Resultados: {model_name} ===")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-score:  {f1:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    return {
        "model_name": model_name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
    }


def main():
    df = load_urls_dataset("data/urls.csv")

    print(f"Dataset cargado correctamente: {len(df)} URLs")

    feature_rows = df["url"].apply(extract_features)
    X = pd.DataFrame(feature_rows.tolist())
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42,
        ),
    }

    results = []

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        result = evaluate_model(model_name, model, X_test, y_test)
        results.append(result)

    results_df = pd.DataFrame(results)

    print("\n=== Comparativa final de modelos ===")
    print(results_df)

    best_model_row = results_df.sort_values(by="f1_score", ascending=False).iloc[0]
    best_model_name = best_model_row["model_name"]

    best_model = models[best_model_name]

    joblib.dump(best_model, "models/phishing_model.pkl")

    print(f"\nMejor modelo seleccionado: {best_model_name}")
    print("Modelo guardado en models/phishing_model.pkl")


if __name__ == "__main__":
    main()