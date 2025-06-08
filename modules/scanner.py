import os
import random

LABELS = {
    "healthy": "The leaf appears healthy. No signs of infection.",
    "yellow": "Detected: Yellow Leaf Curl Virus.",
    "spot": "Detected: Brown Leaf Spot.",
    "mosaic": "Detected: Mosaic Virus.",
    "blight": "Detected: Leaf Blight infection.",
    "rot": "Detected: Root or Stem Rot."
}

def process_leaf_image(filepath: str) -> str:
    """
    Real-time simulation of leaf disease detection based on filename analysis.
    """
    try:
        filename = os.path.basename(filepath).lower()

        for keyword, result in LABELS.items():
            if keyword in filename:
                return f"Prediction: {result}"

        # If no match, randomly assign a result (for demo realism)
        simulated_result = random.choice(list(LABELS.values()))
        return f"Prediction (simulated): {simulated_result}"

    except Exception as e:
        return f"Scan failed: {str(e)}"
