from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Blogs
from django.core.paginator import Paginator , EmptyPage , InvalidPage
# Create your views here.
def index(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()
    lastest = Blogs.objects.all().order_by('-pk')[:2]

    #pagination
    paginator = Paginator(blogs,2)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        blogsPerpage = paginator.page(page)
    except(EmptyPage,InvalidPage):
        blogsPerpage = paginator.page(paginator.num_pages)

    return render(request,"index.html",{'categories':categories,'blogs':blogsPerpage,'lastest':lastest})

