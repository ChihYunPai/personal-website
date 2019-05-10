from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.http import Http404

from .models import Post
from .models import NewTable
from .models import Product
from .models import PhoneProduct

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

def displaydetail(request, sku):
    try:
        requested_product = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('Can not find the requested product no.{}.'.format(sku))
    return render(request, 'displaydetail.html', locals())

def tv(request, tvno=0):
    tv_list = [
        {'name': 'TVBS', 'tvcode': 'Hu1FkdAOws0'},
        {'name': '東森新聞', 'tvcode': 'dxpWqjvEKaM'},
        {'name': '東森財經新聞', 'tvcode': 'tLyxttcv_IY'},
        {'name': '中天新聞', 'tvcode': 'wUPPkSANpyo'},
        {'name': '三立新聞', 'tvcode': '4ZVUmEUFwaY'},
        {'name': '三立iNEWS新聞', 'tvcode': 'fNc3b_f3BFw'},
        {'name': '台視新聞', 'tvcode': 'NbjI0cARzjQ'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'tv.html', locals())

def secondhandphone(request):
    products = PhoneProduct.objects.all()

    return render(request, "secondhandphone.html", locals())