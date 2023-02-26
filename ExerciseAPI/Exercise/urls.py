from django.contrib import admin
from django.urls import path,include
from Exercise.views import *
from rest_framework.routers import DefaultRouter

# router=DefaultRouter()

# router.register(r'Exercise',ExerciseView)
urlpatterns=[
    # path("api/",include(router.urls)),
    # path("", TestViewAPI.as_view(),name="Test")
    path("",ExerciseView.as_view()),
    path("crud/<int:pk>",CRUDExerciseView.as_view())
]