from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page_view(request):
    return render(request,'myapp/home.html')

@login_required
def python_page_view(request):
    return render(request,'myapp/python.html')

@login_required
def java_page_view(request):
    return render(request,'myapp/java.html')

@login_required
def aptitude_page_view(request):
    return render(request,'myapp/aptitude.html')

def logout(request):
    return render(request,'myapp/logout.html')