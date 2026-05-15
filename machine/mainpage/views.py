from django.shortcuts import render

# Create your views here.
def main_page(request):
    models = [
        {
            'name': 'Linear Regression',
            "url":"/predict_linear/"
         },
        {
            "name": "Ridge Regression",
            "url":"/predict_ridge/"
         },
        {
            "name": "Random Forest Regressor",
            "url":"/predict/"
        },
        {
            "name": "Gradient Boosting Regressor",
            "url":"/predict_gradient/"
        },
    ]
    return render(request, "main_page.html", {"models": models})