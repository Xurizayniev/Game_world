from django.urls import path
from .views import *
from config import settings
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', loginview, name='login'),
    path('', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    
    path('register/', user_registration, name='registration'),

]