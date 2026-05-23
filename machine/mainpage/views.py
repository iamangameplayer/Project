from django.shortcuts import render

# Create your views here.
def main_page(request):
    models = [
        {
            'name': 'Linear Regression',
            "url":"/predict_linear/",
            "icon":"📈",
            "description":"A simple regression model that predicts values using a linear relations between features and targets",
         },
        {
            "name": "Ridge Regression",
            "url":"/predict_ridge/",
            "icon":"📊",
            "description":"An improved linear regression model that uses regularization to reduce overfitting and improve generalization"

         },
        {
            "name": "Random Forest Regressor",
            "url":"/predict/",
            "icon": "🌲",
            "description": "An ensemble learning model that combines multiple decision trees for more accurate predictions"
        },
        {
            "name": "Gradient Boosting Regressor",
            "url":"/predict_gradient/",
            "icon":"🚀",
            "description":"A powerful boosting algorithm that builds models sequentially to minimize prediction errors and improve performance",
        },
    ]
    return render(request, "main_page.html", {"models": models})