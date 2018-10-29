from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#跳转首页
from home_page_app.models import Category, Book


def index_page(request):
    return render(request,'commodity_management_app/index.html')

#增加商品跳转
def add_page(request):
    cate_2 = Category.objects.filter(category_pid__isnull=False)
    return render(request,'commodity_management_app/main/add.html',{"cate_2":cate_2})

#异步增加商品
def add_ajax(request):
    #获取书籍的二级分类名称
    category2_name = request.POST.get("category2_name")
    cate_2 = Category.objects.filter(category_name=category2_name)
    cate_1 = Category.objects.filter(category_id=cate_2[0].category_pid)
    book_name = request.POST.get("book_name")
    book_author = request.POST.get("book_author")
    book_publish = request.POST.get("book_publish")
    publish_time = request.POST.get("publish_time")
    shelves_date = request.POST.get("shelves_date")
    Book(book_name=book_name,book_author=book_author,book_publish=book_publish,publish_time=publish_time,shelves_date=shelves_date,book_category=cate_2[0]).save()
    return HttpResponse("1")

#商品列表跳转
def list_page(request):
    book = Book.objects.all()
    length = len(book)
    #接收请求参数：明确要查询的页号
    page_num = request.GET.get("num")
    if not page_num:
        page_num = 1
    page = Paginator(object_list=book,per_page=15).page(page_num)
    return render(request,'commodity_management_app/main/list.html',{"page":page,"length":length})

#增加商品父类别
def category_1(request):
    return render(request,'commodity_management_app/main/zjsp.html')

#增加商品父类别异步
def category_1_ajax(request):
    category_1 = request.POST.get("category_1")
    Category(category_name=category_1).save()
    return HttpResponse("1")

#增加子类别
def category_2(request):
    category_1 = Category.objects.filter(category_pid__isnull=True)
    return render(request,'commodity_management_app/main/zjzlb.html',{"category_1":category_1})

#增加子类别异步
def category_2_ajax(request):
    #获取二级类别名称
    category_2 = request.POST.get("category_2")
    #获取一级类别名称
    category_1 = request.POST.get("category_1")
    category1 = Category.objects.filter(category_name=category_1)
    Category(category_name=category_2,category_pid=category1[0].category_id).save()
    return HttpResponse("1")

#商品列表跳转
def category_list(request):
    book = Book.objects.all()
    length = len(book)
    l= []

    l2 = []

    l1 = []
    for i in book:
        l.append(i.book_name)
        l2.append(i.book_category.category_pid)
    print(l)
    print(l2)
    for i in l2:
        l1.append(i)
    #接收请求参数：明确要查询的页号
    page_num = request.GET.get("num")
    if not page_num:
        page_num = 1
    page = Paginator(object_list=book,per_page=15).page(page_num)
    return render(request,'commodity_management_app/main/splb.html',{"page":page,"length":length,"l2":l2,"l1":l1})