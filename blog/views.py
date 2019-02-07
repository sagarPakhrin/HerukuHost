from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def home(request):
    return render(request,'blog/home.html')
def about(request):
    return render(request,'blog/about.html')
