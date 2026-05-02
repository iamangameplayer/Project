from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import joblib
# Create your views here.
linear_model = joblib.load(open(r"C:\Users\nagas\PycharmProjects\Linear_Regression\linear_regression.joblib","rb"))


def home(request):
    return render(request, 'linear_regression.html')

@csrf_exempt
def predict_linear(request):
        if request.method == 'POST':
            features = [
            float(request.POST.get('MedInc')),
            float(request.POST.get('HouseAge')),
            float(request.POST.get('AveRooms')),
            float(request.POST.get('AveBedrms')),
            float(request.POST.get('Population')),
            float(request.POST.get('AveOccup')),
            float(request.POST.get('Latitude')),
            float(request.POST.get('Longitude')),
        ]

        prediction = linear_model.predict([features])
        print("Features", features)
        print("Prediction", prediction)
        return JsonResponse({'result': float(prediction[0])})