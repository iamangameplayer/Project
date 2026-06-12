from django.shortcuts import render

def metrics(request):
    return render(request, 'metrics_page.html')


def model_comparison(request):
    models = [

        {
            "name": "Linear Regression",
            "r2":0.62,
            "mae":0.50,
            "mse":0.51,
            "rmse":0.72,
        },

        {
            "name": "Ridge Regression",
            "r2":0.59,
            "mae":0.54,
            "mse":0.54,
            "rmse":0.74,
        },
        {
            "name": "Random Forest Regression",
            "r2":0.32,
            "mae":0.28,
            "mse":0.28,
            "rmse":0.28,
        },
        {
            "name": "Gradient Boosting Regression",
            "r2":0.32,
            "mae":0.28,
            "mse":0.28,
            "rmse":0.28,
        },
        {
            "name": "KNN Regression",
            "r2":0.32,
            "mae":0.28,
            "mse":0.28,
            "rmse":0.28,
        },
        {
            "name": "XGBoost Regression",
            "r2":0.32,
            "mae":0.28,
            "mse":0.28,
            "rmse":0.28,
        }
    ]

    return render(request,
"model_comparison.html", {"models":models,"best_model":"XGBoost Regression"})