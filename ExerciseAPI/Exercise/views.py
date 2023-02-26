from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ExercisesAPI
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class=ExerciseAPISerializer
    queryset=ExercisesAPI.objects.all()


class TestViewAPI(APIView):

    permission_classes=(IsAuthenticated,)

    def get(self,request,*args, **kwargs):
        qs= ExercisesAPI.objects.all()
        serializer=ExerciseAPISerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args, **kwargs):
        serializer=ExerciseAPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        