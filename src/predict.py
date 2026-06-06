import joblib
import pandas as pd

from features import extract_features


def explain_prediction(features: dict, url: str) -> list[str]:
    reasons = []

    suspicious_tlds = [".ru", ".xyz", ".tk", ".top", ".click"]

    if features["has_https"] == 0:
        reasons.append("La URL no utiliza HTTPS.")

    if features["suspicious_keyword_count"] > 0:
        reasons.append(
            "La URL contiene palabras sospechosas relacionadas con phishing."
        )

    if features["hyphen_count"] >= 2:
        reasons.append(
            "La URL contiene varios guiones, algo habitual en dominios fraudulentos."
        )

    if features["url_length"] > 50:
        reasons.append("La URL tiene una longitud elevada.")

    if features["digit_count"] >= 3:
        reasons.append("La URL contiene varios números.")

    if features["has_ip"] == 1:
        reasons.append("La URL utiliza una dirección IP en lugar de un dominio.")

    if features["subdomain_count"] >= 2:
        reasons.append("La URL contiene varios subdominios.")

    for tld in suspicious_tlds:
        if tld in url.lower():
            reasons.append(f"La URL utiliza un dominio potencialmente sospechoso: {tld}")

    if not reasons:
        reasons.append(
            "La URL no activa reglas simples, pero el modelo la clasifica como phishing por los patrones aprendidos durante el entrenamiento."
        )

    return reasons


def main():
    model = joblib.load("models/phishing_model.pkl")

    url = input("Introduce una URL para analizar: ").strip()

    features = extract_features(url)
    X_new = pd.DataFrame([features])

    prediction = model.predict(X_new)[0]
    probability = model.predict_proba(X_new)[0]

    print("\n=== Resultado del análisis ===")
    print(f"URL: {url}")
    print(f"Predicción: {'Phishing' if prediction == 1 else 'Legítima'}")
    print(f"Probabilidad legítima: {probability[0]:.4f}")
    print(f"Probabilidad phishing: {probability[1]:.4f}")

    print("\n=== Explicación de la predicción ===")
    reasons = explain_prediction(features, url)

    for reason in reasons:
        print(f"- {reason}")

    print("\n=== Características extraídas ===")
    for key, value in features.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()