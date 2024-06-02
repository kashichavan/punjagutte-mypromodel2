from django.urls import path
from .views import register,getdata
app_name='app1'
urlpatterns = [
    path('register/',register,name='register'),
    path('getdata/',getdata,name='getdata'),
]
