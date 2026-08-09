from django.shortcuts import render
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


model_ridge = joblib.load(r"ridge_regression.joblib",'r')

def home(request):
    return render(request,'ridge_page.html')

@csrf_exempt
def predict_ridge(request):
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
            print("CRASH",e)
            return JsonResponse({'error': str(e)})
        prediction = model_ridge.predict([features])
        return JsonResponse({'result': float(prediction[0])})
