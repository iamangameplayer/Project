import urllib.request
from pathlib import Path

MODEL_URL = "https://github.com/iamangameplayer/Project/releases/download/v1.0/regressor_bundled.joblib"

MODEL_PATH = Path(__file__).resolve().parent / "regression" / "regressor_bundled.joblib"

print("Downloading ML model...")

urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

print("ML model downloaded successfully.")
