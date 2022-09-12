from django.shortcuts import render
from django.http import HttpResponse
from  .models import ToDoList, Item

# Create your views here.
def index1(response, id):
    ls = ToDoList.objects.get(id=id)

    return render(response, "mainApp/list.html", {"ls":ls})
    #return render(response, "mainApp/base.html", {"name":ls.name})


def home(response):
    return render(response, "mainApp/home.html", {"name": "test"})

def page1(response):

    return render(response, "mainApp/page1.html", {"name": "name"})



