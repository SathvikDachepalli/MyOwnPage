from django.contrib import admin
from django.urls import path,include
from ExerciseAPI.views import ExerciseView
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="Website"
admin.site.site_title="Page"
admin.site.index_title="Welcome Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include('ExerciseAPI.urls')),
    path("",include('MyPage.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
