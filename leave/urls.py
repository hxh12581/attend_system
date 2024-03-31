from django.urls import path
from .views import *

urlpatterns = [
    path('', leave_message, name='leave_message'),
    path('leave_add_show/', leave_add_show, name='leave_add_show'),
    path('leave_update_show/<int:id>/', leave_update_show, name='leave_update_show'),
    # path('leave_pop_show/', leave_pop_show, name='leave_pop_show'),

    path('leave_add/add/', leave_add, name='leave_add'),
    path('leave_update/update/<int:id>/', leave_update, name='leave_update'),
    path('leave_pop/pop/<int:id>/', leave_pop, name='leave_pop'),


]
