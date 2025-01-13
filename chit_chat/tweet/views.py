from django.shortcuts import render
# import templates
# Create your views here
def index(request):
    return render(request , "index.html")