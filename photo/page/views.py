from django.shortcuts import render
from.models import Contact
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'page/home.html')

def about(request):
    return render(request,'page/about.html')

def contact(request):
    if request.method=="POST" :
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        massage=request.POST.get('massage')
        contact=Contact(name=name,email=email,subject=subject,massage=massage)
        contact.save()
        return HttpResponse("<h1>THANK U FOR CONTACTING</h1>")
        
        
    return render(request,'page/contact.html')