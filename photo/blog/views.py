from django.shortcuts import render
from . models import Blog

# Create your views here.

def blog(request):
    post=Blog.objects.all()#create copy of the blog class and save in post
    #then send the post to html
    return render(request,'blog/blog.html',{'post':post})

#from tamplet
