from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples = [{'name': "Shilpa" , 'age': 29},
               {'name':"kecho", 'age': 17},
               {'name':"Niraj" , 'age': 27}]

    vegies = ["cucumber","tomto", "potato"]

    return render(request,"index.html", context={'peoples' : peoples , "vegies": vegies})


def success_page(request):
    context = {'page': 'success_page'}
    my_list = ["bigda","ML","data"]

    return render(request,"index.html",context={'page':'success_page', "my_list": my_list})