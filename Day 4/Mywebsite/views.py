

#Step 1.1 
from django.http import HttpResponse
#step 3.1
from django.shortcuts import render

#step 3.2
def homepage(request):
    return render(request,"index.html")


def aboutus(request):
    return HttpResponse("<b>Hello my  New django project </b>")
    #step1.2 :go to url's.py file


def new(request):
    return HttpResponse("<b>new rendered </b>")

#stpe 2.1 for dynamic url , go to url's.py 
def drouting(request, id):
    return HttpResponse(id)