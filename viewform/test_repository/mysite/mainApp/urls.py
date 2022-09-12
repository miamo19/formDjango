from django.urls import path
from . import views

urlpatterns =[
    path("", views.home, name= "home"),
    path("page", views.page1, name= "page1"),
    path("<int:id>", views.index1, name="index"),
]