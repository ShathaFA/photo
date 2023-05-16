from django.shortcuts import render

# Create your views here.
def baby(request):
    return render(request,'gallery/baby.html')#from tamplet

def product(request):
    return render(request,'gallery/product.html')#from tamplet
def country(request):
    return render(request,'gallery/country.html')#from tamplet