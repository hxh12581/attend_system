from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('regist/', regist, name='regist'),
    path('index/', index, name='index'),
    path('', loginout, name='loginout')
]
