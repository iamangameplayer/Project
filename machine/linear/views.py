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
        try:
            MedInc = float(request.POST.get('MedInc') or 0)
            HouseAge = float(request.POST.get('HouseAge') or 0)
            AveRooms = float(request.POST.get('AveRooms') or 0)
            AveBedrms = float(request.POST.get('AveBedrms') or 0)
            Population = float(request.POST.get('Population') or 0)
            AveOccup = float(request.POST.get('AveOccup') or 0)
            Latitude = float(request.POST.get('Latitude') or 0)
            Longitude = float(request.POST.get('Longitude') or 0)

            rooms_per_person = AveRooms/AveOccup if AveOccup!=0 else 0
            bedrooms_per_person = AveBedrms/AveOccup if AveOccup!=0 else 0
            average_income_per_block = MedInc/Population if Population!=0 else 0

            features = [
            MedInc,HouseAge,AveRooms,AveBedrms,Population,
                AveOccup,Latitude,Longitude,
                rooms_per_person,bedrooms_per_person,
            average_income_per_block,]
        except Exception as e:
            print("CRASH",e)
            return JsonResponse({'error': str(e)})

        prediction = linear_model.predict([features])
        #print("Features", features)
        #print("Prediction", prediction)
        return JsonResponse({'result': float(prediction[0]*100000)})
