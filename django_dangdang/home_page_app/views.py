from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.


from home_page_app.models import Category, Book


#查询二级列表所归属的一级列表
from user_app.models import User


def filter_cate2(category_id):
    cate2 = Category.objects.filter(category_pid=category_id)
    return cate2 if cate2 else []

#跳转首页
def home_page(request):
    #获取一级列表QuerySet
    cate_1 = Category.objects.filter(category_pid__isnull=True)
    #获取用户登录状态
    flag = request.GET.get("flag")
    user_email = request.GET.get("user_email")
    print(user_email)
    user = User.objects.filter(user_email=user_email)
    print(user)
    # if flag == "1":
    #     User(user_status=user.).save()
    # else:
    #     User(user_status=0).save()
    #获取一级二级列表列表
    catelist = [(i,filter_cate2(i.category_id)) for i in cate_1]
    #获取书籍信息
    book = Book.objects.all()
    book1 = Book.objects.filter(shelves_date__month=datetime.now().month)[:8]
    book2 = Book.objects.filter(shelves_date__month=datetime.now().month).order_by("-sales")[:5]
    book3 = Book.objects.all()[:8]
    book4 = Book.objects.filter(shelves_date__month=datetime.now().month).order_by("-sales")[:11]
    return render(request,'home_page/index.html',{'catelist':catelist,'book':book,'book1':book1,'book2':book2,"book3":book3,'book4':book4,'flag':flag,"user":user})


#跳转到商品分类页面
def book_category_list(request):
    #获取一级类别id
    cate1 = request.GET.get("category1_id")
    #获取二级类别id
    cate2 = request.GET.get("category2_id")
    #获取用户登录状态
    flag = request.GET.get("flag")
    #获取用户昵称
    user_name = request.GET.get("user_name")
    #获取用户需要跳转的分页
    page_num = request.GET.get("num")
    #获取用户的查询方式编号
    cursort = request.GET.get("cur_sort")
    print(cursort)
    if not cursort:
        cursort = 0
    #如果二级id存在，说明点的是二级id，显示二级类别所对应的图书
    if cate2:
       cate_2 = Category.objects.filter(category_id=cate2)
       cate_1 = Category.objects.filter(category_id=cate_2[0].category_pid)
       cate_2_2 = Category.objects.filter(category_pid=cate_1[0].category_id)
       #按查询方式查询
       if cursort == "1":
            book = Book.objects.filter(book_category=cate2).order_by("sales")
       elif cursort == "2":
            print("haha")
            book = Book.objects.filter(book_category=cate2).order_by("book_dprice")
       elif cursort == "3":
            book = Book.objects.filter(book_category=cate2).order_by("publish_time")
       else:
            book = Book.objects.filter(book_category=cate2)

       # for i in book1:
       #     book = i
       if not page_num:
           page_num=1
       page = Paginator(object_list=book, per_page=4).page(page_num)
       return render(request,'book_category_list/booklist.html',{"page":page,"cate_1":cate_1,"cate_2":cate_2,"cate_3":cate_2,"cate_2_2":cate_2_2,"book":book,'cate1':cate1,"cate2":cate2,"cursort":cursort,"flag":flag,"user_name":user_name})
    else:
        #先获取一级分类
        cate_1 = Category.objects.filter(category_id=cate1)
        #获取当前一级分类下的二级分类
        l=[]
        cate_2 = Category.objects.filter(category_pid=cate_1[0].category_id)
        for i in cate_2:
            l.append(i.category_id)
        #根据获取的二级分类id进行查询
        if cursort == "1":
            book = Book.objects.filter(book_category__in=l).order_by("sales")
        elif cursort == "2":
            book = Book.objects.filter(book_category__in=l).order_by("book_dprice")
            print("heelo")
        elif cursort == "3":
            book = Book.objects.filter(book_category__in=l).order_by("publish_time")
        else:
            book = Book.objects.filter(book_category__in=l)
        print(book)
        if not page_num:
            page_num=1
        page = Paginator(object_list=book, per_page=4).page(page_num)
        print(page)
        return render(request, 'book_category_list/booklist.html', {"page": page,"cate_1":cate_1,"cate_3":cate_1,"cate_2_2":cate_2,'l':l,"book":book,'cate1':cate1,"cursort":cursort,"flag":flag,"user_name":user_name})

#获取书籍详细信息跳转页面
def book_details(request):
    #获取书籍id
    book_id = request.GET.get("book_id")
    # 获取一级类别id
    cate1 = request.GET.get("category1_id")
    # 获取二级类别id
    cate2 = request.GET.get("category2_id")
    # 获取用户登录状态
    flag = request.GET.get("flag")
    # 获取用户昵称
    user_name = request.GET.get("user_name")
    #获取当前书籍对象
    book = Book.objects.filter(book_id=book_id)
    print(book)
    # 如果二级id存在，说明点的是二级id，显示二级类别所对应的图书
    if cate2:
        cate_2 = Category.objects.filter(category_id=cate2)
        cate_1 = Category.objects.filter(category_id=cate_2[0].category_pid)
    # 如果二级id存在，说明点的是二级id，显示二级类别所对应的图书
    # cate_2 = Category.objects.filter(category_id=book[0].book_category.category)
    # cate_1 = Category.objects.filter(category_id=cate_2[0].category_pid)
        return render(request, 'book_details/Book details.html',{ "cate_1": cate_1, "cate_2": cate_2, "book": book,"cate_1_1":cate_1,"cate_2_2":cate_2,"cate1":cate1,"cate2":cate2,"flag":flag,"user_name":user_name})
    else:
        # 先获取一级分类
        cate_1 = Category.objects.filter(category_id=cate1)
        cate_2 = Category.objects.filter(category_pid=cate_1[0].category_id)
        return render(request, 'book_details/Book details.html', {"cate_1": cate_1, "book": book,"cate_1_1":cate_1,"cate_2_2":cate_2,"cate1":cate1,"cate2":cate2,"flag":flag,"user_name":user_name})
























