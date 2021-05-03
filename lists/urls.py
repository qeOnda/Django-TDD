from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('lists/the-only-list-in-the-world/', views.view_list, name="view_list")
]