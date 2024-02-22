

#Step 1 
from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("<b>Hello my  New django project </b>")
    #step2 :go to url's.py file



def new(request):
    return HttpResponse("<b>new rendered </b>")

