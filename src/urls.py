from django.urls import path
from .views import index,get_data


urlpatterns = [
    path('', index,name='index'),
    path('upload', get_data,name='get_data'),
]