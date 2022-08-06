
from django.contrib import admin
from django.urls import path
from .views import index , blogDetails
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('blog/<int:id>',blogDetails,name="blogDetail"),

]
