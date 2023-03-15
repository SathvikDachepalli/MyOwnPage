from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
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
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)