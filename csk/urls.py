from django.urls import path
from csk.views import *
app_name='nothing'
urlpatterns = [
    path('msd/',msd,name='msd'),
]
