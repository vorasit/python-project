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

    # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    #บทความเเนะนำ
    suggestion = Blogs.objects.all().order_by('-views')[:3]

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

    return render(request,"index.html",{'categories':categories,'blogs':blogsPerpage,'lastest':lastest,'popular':popular,'suggestion':suggestion})

def blogDetails(request,id):
    singleBlog = Blogs.objects.get(id=id)
    singleBlog.views = singleBlog.views+1
    singleBlog.save()

        # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    #บทความเเนะนำ
    suggestion = Blogs.objects.all().order_by('-views')[:3]

    return render(request,"frontend/blogDetail.html",{'blog':singleBlog,'popular':popular,'suggestion':suggestion})

def searchCategory(request,category_id):
    blogs = Blogs.objects.filter(category_id = category_id)

     # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    #บทความเเนะนำ
    suggestion = Blogs.objects.all().order_by('-views')[:3]

    categoryName = Category.objects.get(id=category_id)
    categories = Category.objects.all()

    return render(request,"frontend/searchCategory.html",{"blogs":blogs,'categories':categories,'popular':popular,'suggestion':suggestion,'categoryName':categoryName})

def searchWriter(request,writer):
    blogs = Blogs.objects.filter(writer=writer)
    # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    #บทความเเนะนำ
    suggestion = Blogs.objects.all().order_by('-views')[:3]

    categories = Category.objects.all()

    return render(request,"frontend/searchWriter.html",{'blogs':blogs,'categories':categories,'popular':popular,'suggestion':suggestion,'writer':writer})
