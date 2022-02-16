from django.contrib import admin
from django.urls import path, include

admin.site.site_header ="its cold frozzen site"
admin.site.site_title ="its site title here site"
admin.site.index_title ="its cold index title here site"



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls"))
]
