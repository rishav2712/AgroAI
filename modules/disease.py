import os
import joblib

# Load pre-trained vectorizer and model
# These should be trained offline and saved in the 'models/' folder
VECTORIZER_PATH = os.path.join("models", "symptom_vectorizer.pkl")
MODEL_PATH = os.path.join("models", "symptom_classifier.pkl")

try:
    vectorizer = joblib.load(VECTORIZER_PATH)
    classifier = joblib.load(MODEL_PATH)
except Exception as e:
    vectorizer = None
    classifier = None
    print(f"Warning: ML model or vectorizer not found. Falling back to rule-based logic. ({e})")

# Fallback rules (for safety)
def fallback_rules(symptoms: str) -> str:
    symptoms = symptoms.lower().strip()

    if not symptoms:
        return "Please describe the symptoms to get a diagnosis."

    if "yellow" in symptoms and "leaf" in symptoms:
        if "curl" in symptoms or "edges" in symptoms:
            return "Diagnosis: Yellow Leaf Curl Virus"
        return "Diagnosis: General Yellowing - Possible nutrient deficiency"
    elif "spots" in symptoms and "brown" in symptoms:
        return "Diagnosis: Brown Leaf Spot - Fungal infection likely"
    elif "black" in symptoms and "rot" in symptoms:
        return "Diagnosis: Black Rot - Bacterial disease"
    elif "wilt" in symptoms:
        return "Diagnosis: Wilting - Possibly Fusarium or Bacterial Wilt"
    elif "mosaic" in symptoms:
        return "Diagnosis: Mosaic Virus"
    else:
        return "Diagnosis unclear. Please consult an agricultural expert."

# Primary interface function
def predict_disease(symptoms: str) -> str:
    if not symptoms.strip():
        return "Please enter symptoms to diagnose."

    if vectorizer and classifier:
        try:
            X = vectorizer.transform([symptoms])
            prediction = classifier.predict(X)
            return f"Diagnosis (ML): {prediction[0]}"
        except Exception as e:
            return f"ML prediction failed: {e}"

    # Fallback
    return fallback_rules(symptoms)
