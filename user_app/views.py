from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request,'user_app/display.html') #render template

def index(request):
    return render(request,'user_app/index.html') #render template