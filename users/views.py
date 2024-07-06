from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CarSerializer, UserSerializer
from .models import Cars


class CarApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk=None):
        if pk:
            car_id = Cars.objects.get(pk=pk)
            car = CarSerializer(car_id)
            return Response(car.data)
        else:
            cars = Cars.objects.filter(car_active=True)
            cars_list = CarSerializer(cars, many=True)
            return Response(cars_list.data)


class CarCreateUpdateApiView(APIView):
    permission_classes = [IsAdminUser, ]

    def get(self, request):
        cars = Cars.objects.all()
        cars_list = CarSerializer(cars, many=True)
        return Response(cars_list.data)

    def post(self, request):
        car_create = CarSerializer(data=request.data)
        if car_create.is_valid():
            car_create.save()
            return Response(car_create.data, status.HTTP_201_CREATED)
        else:
            return Response(car_create.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk:
            car_info = Cars.objects.get(pk=pk)
            if request.method == 'PUT':
                car_update = CarSerializer(car_info, data=request.data)
                if car_update.is_valid():
                    car_update.save()
                    return Response(car_update.data, status=status.HTTP_200_OK)
                else:
                    return Response(car_update.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if pk:
            car_info = Cars.objects.get(pk=pk)
            if request.method == 'PATCH':
                car_update = CarSerializer(car_info, data=request.data, partial=True)
                if car_update.is_valid():
                    car_update.save()
                    return Response(car_update.data, status=status.HTTP_200_OK)
                else:
                    return Response(car_update.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDeleteApiView(APIView):
    permission_classes = [IsAdminUser, ]

    def delete(self, request, pk=None):
        if pk:
            car_info = Cars.objects.get(pk=pk)
            if request.method == 'DELETE':
                car_info.delete()
                return Response('Mashina muvaffaqiyatli ochib ketdi', status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarBuyApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        id = request.data.get('id')
        if id:
            try:
                car = Cars.objects.get(id=id)
            except Cars.DoesNotExist:
                return Response({'error': "Car is not fount"})
            else:
                if car.car_active == True:
                    car.car_active = False
                    car.save()
                    if car.car_active == False:
                        return Response({'detail': "Mashinani muvaffaqiyatli band qildingiz."},
                                        status=status.HTTP_201_CREATED)
