from django.contrib import admin
from django.urls import path,include
from Exercise.views import ExerciseView
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="Exercise API"
admin.site.site_title="Exercise page"
admin.site.index_title="Welcome Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Exercise.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
