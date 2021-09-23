from django.shortcuts import render
from newsapp.models import Post

# Create your views here.
def news(request):
    posts=Post.objects.all()
    return render(request,"news/news.html",{"posts" : posts})