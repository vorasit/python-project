
from django.contrib import admin
from django.urls import path
from .views import index , blogDetails,searchCategory,searchWriter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('blog/<int:id>',blogDetails,name="blogDetail"),
    path('blog/category/<int:category_id>',searchCategory,name="searchCategory"),
    path('blog/writer/<str:writer>',searchWriter,name="searchWriter")

]
