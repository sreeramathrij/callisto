from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def index(request, year, *args, **kwargs):
    year = year
    
    return render(request, "")
    