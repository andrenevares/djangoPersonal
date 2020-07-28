from django.shortcuts import render
from django.http import HttpResponse

def blog_main(request):
    
    return render (request, 'blog/index.html')