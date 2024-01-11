
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from footfiesta import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("footapp.urls")),
]


