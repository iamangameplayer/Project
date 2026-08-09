
import urllib.request
from pathlib import Path

MODEL_URL = "https://github.com/iamangameplayer/Project/releases/download/v1.0/regressor_bundled.joblib"

MODEL_PATH = (
    Path(__file__).resolve().parent
    / "regression"
    / "regressor_bundled.joblib"
)

MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

print("Downloading ML model...")
print(f"Destination: {MODEL_PATH}")

urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

print("ML model downloaded successfully.")
print(f"Model exists: {MODEL_PATH.exists()}")
print(f"Model size: {MODEL_PATH.stat().st_size / (1024 * 1024):.2f} MB")
