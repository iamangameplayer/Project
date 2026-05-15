from django.http import JsonResponse
import joblib
from django.shortcuts import render


model_gradient = joblib.load(r"C:\Users\nagas\PycharmProjects\Linear_Regression\gradient_boosting_regressor.joblib",)
def home(request):
    return render(request, 'gradient_page.html')
def predict_gradient(request):
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

            prediction = model_gradient.predict([features])

            return JsonResponse({'result': float(prediction[0])})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)