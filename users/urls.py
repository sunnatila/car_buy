from django.urls import path
from .views import CarApiView, CarCreateUpdateApiView, UserAPIView, CarBuyApiView, CarDeleteApiView

urlpatterns = [
    path('api/v1/cars/', CarApiView.as_view()),
    path('api/v1/cars/<int:pk>/', CarApiView.as_view()),
    path('api/v1/car/create/', CarCreateUpdateApiView.as_view()),
    path('api/v1/car/update/<int:pk>/', CarCreateUpdateApiView.as_view()),
    path('api/v1/car/patch/<int:pk>/', CarCreateUpdateApiView.as_view()),
    path('api/v1/car/delete/<int:pk>/', CarDeleteApiView.as_view()),
    path('api/v1/car_buy/', CarBuyApiView.as_view()),
    path('api/v1/signup/', UserAPIView.as_view()),
]
