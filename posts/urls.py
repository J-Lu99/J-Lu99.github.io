from django.urls import path
from .views import home_view,post_view

urlpatterns = [
    path("",home_view.as_view(),name="home"),
    path("messages/",post_view.as_view(),name="messages"),
]
