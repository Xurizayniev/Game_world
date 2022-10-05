from django.urls import path
from .views import *

app_name = 'users'


urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', loginview, name='login'),
    path('logout/', logout, name='logout'),
    
    # path('registration/', user_registration, name='registration'),

]