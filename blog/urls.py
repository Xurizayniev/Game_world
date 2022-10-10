from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='news'),
    path('<int:pk>/', blogdetail, name='detail'),
    # path('create/', create_post, name='create'),
]
