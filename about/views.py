from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def about_me(request):
    return HttpResponse("This is going to be an about page")