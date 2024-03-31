from django.urls import path
from .views import *

urlpatterns = [
    path('', attend_message, name='attend_message'),
    path('attend_sign_in/', attend_sgin_in, name='attend_sign_in'),
    path('attend_sign_out/', attend_sign_out, name='attend_sign_out'),
    path('attend_sign_in/sgin/', sgin, name='sign'),
    path('attend_sign_out/out/', out, name='out'),
]
