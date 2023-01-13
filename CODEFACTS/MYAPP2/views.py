from django.shortcuts import render, HttpResponse, redirect
from MYAPP2.models import Contact

# Create your views here.

def index(request):
    return  render(request, 'home.html')
    
def about(request):
     return  render(request,'about.html')

def python(request):
     return  render(request,'pyth.html')

def contactus(request):   
     if request.method !="POST":
          return render(request,'contact.html')
     else:
          name = request.POST.get('name')
          email = request.POST.get('email')
          description = request.POST.get('description')
          P = Contact.objects.create(name=name, email=email,desc=description)
          return render(request, 'home.html')
     