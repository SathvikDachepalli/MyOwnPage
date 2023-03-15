from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Exercise.views import *

urlpatterns=[ 
    path("",ExerciseView.as_view()),
    path("/crud/<int:pk>",CRUDExerciseView.as_view())
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)