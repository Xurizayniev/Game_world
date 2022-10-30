from django.urls import path
from .views import *

app_name = 'games'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list', GameListView.as_view(), name='list'),
    path('games/detail/<int:pk>/', GameDetail, name='detail'),
    path('games/trailer/', VideoListView.as_view(), name='trailer'),
    path('add_cart/<int:id>/', update_cart_view, name='add'),

]
