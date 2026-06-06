from features import extract_features

url = "https://www.google.com"
features = extract_features(url)

print("URL analizada:")
print(url)
print("\nCaracterísticas extraídas:")
for key, value in features.items():
    print(f"{key}: {value}")