
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Bibek Admin"
admin.site.site_title = "Hello Bibek Bhattarai"
admin.site.index_title = "Django_project_01 dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
]
