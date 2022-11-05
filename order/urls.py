from django.urls import path
from .views import *


app_name = 'order'

urlpatterns = [
    path('checkout/', checkoutview, name='checkout'),
    path('profile/', profile, name='profile')
]