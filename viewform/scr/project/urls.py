"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Blog2.views import (
product_create_view,
product_update_view,
product_list_view,
product_delete_view,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog2/create', product_create_view, name=''),
    path('blog2/<int:id>/delete', product_delete_view, name=''),
    path('blog2/', product_list_view, name='list'),
    path('blog2/update/<int:id>', product_update_view, name='update'),
    path('', include('Blog.urls')),

]
