from django.shortcuts import render
from newsapp.models import Category, Post

# Create your views here.
def news(request):
    posts=Post.objects.all()
    return render(request,"news/news.html",{"posts" : posts})

def category(request, category_id):
    category=Category.objects.get(id=category_id)
    posts=Post.objects.filter(categories=category)
    return render(request,"news/categories.html",{'category':category,'posts':posts})