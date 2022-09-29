from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact')

]
