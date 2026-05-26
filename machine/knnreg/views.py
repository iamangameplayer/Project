from django.shortcuts import render
from joblib import load
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

model_knn=load(r"C:\Users\nagas\PycharmProjects\Linear_Regression\knn_regression.joblib")

def home(request):
    return render(request, "knn_page.html")

@csrf_exempt
def predict_knn(request):
    if request.method == "POST":
        try:
            features = [
                float(request.POST.get("MedInc") or 0),
                float(request.POST.get("HouseAge") or 0),
                float(request.POST.get("AveRooms") or 0),
                float(request.POST.get("AveBedrms") or 0),
                float(request.POST.get("Population") or 0),
                float(request.POST.get("AveOccup") or 0),
                float(request.POST.get("Latitude") or 0),
                float(request.POST.get("Longitude") or 0),
            ]
        except Exception as e:
            print("CRASH",e)
            return JsonResponse({"error":str(e)})
        prediction = model_knn.predict([features])
        return JsonResponse({"result":float(prediction[0])})