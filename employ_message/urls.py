from django.urls import path
from .views import *

urlpatterns = [
    path('', employ_message, name='employ_message'),
    path('update/', employ_message_update, name='employ_message_update'),
    path('insert/', employ_message_insert, name='employ_message_insert'),
    path('cancel/', employ_message_cancel, name='employ_message_cancel'),
]
