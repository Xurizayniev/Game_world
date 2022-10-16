from django.urls import path
from .views import *

app_name = 'games'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('games/detail/<int:pk>/', GameDetail, name='detail'),
    path('games/trailer/', VideoListView.as_view(), name='trailer')
]
