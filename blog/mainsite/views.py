from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Post
from .models import NewTable
from .models import Product

from datetime import datetime

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) + str(post) + "<hr>")
    #     post_lists.append(
    #         "<small>" + str(post.text) + "</small><br><br>")
    # return HttpResponse(post_lists)

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post is not None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

def about(request):
    return render(request, 'about.html', locals())

def productlist(request):
    products = Product.objects.all()
    return render(request, 'productlist.html', locals())