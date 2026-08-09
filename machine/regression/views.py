from django.views.decorators.csrf import csrf_exempt
import joblib
from django.shortcuts import render
from django.http import JsonResponse


from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parent / "regressor_bundled.joblib"

model = joblib.load(MODEL_PATH)
def home(request):
    return render(request, 'index.html')

@csrf_exempt
def predict(request):
        if request.method == 'POST':
            try:
                features = [
                float(request.POST.get('MedInc') or 0),
                float(request.POST.get('HouseAge') or 0),
                float(request.POST.get('AveRooms') or 0),
                float(request.POST.get('AveBedrms') or 0),
                float(request.POST.get('Population') or 0),
                float(request.POST.get('AveOccup') or 0),
                float(request.POST.get('Latitude') or 0),
                float(request.POST.get('Longitude') or 0),
                ]
            except Exception as e:
                print("CRASH", e)
                return JsonResponse({'error': str(e)})
            prediction = model.predict([features])
            print("Features", features)
            print("Prediction", prediction)
            return JsonResponse({'result': float(prediction[0]*10000)})

