from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

#展示购物车
from cart_app.cart import Cart
from user_app.models import User


def shopping_cart(request):
    # 获取用户登录状态
    flag = request.GET.get("flag")
    # 获取用户昵称
    user_name = request.GET.get("user_name")
    # 先从session获取到购物车
    shopping_cart = request.session.get("shopping_cart")
    if flag == "1":
        user = User.objects.get(user_name=user_name)
        print(user)
        return render(request, 'cart_app/index/car.html',{"flag":flag,"user_name":user_name,"shopping_cart":shopping_cart,"user":user})
    else:
        return render(request, 'cart_app/index/car.html',{"shopping_cart": shopping_cart})
    # else:
    #     return render(request, 'cart_app/index/car.html',{"flag": flag, "user_name": user_name, "shopping_cart": shopping_cart})

#添加购物车
def addBookToCart(request):
    #获取书籍的id
    book_id = int(request.GET.get("book_id"))
    print(book_id)
    #获取书籍的数量
    amount = int(request.GET.get("amount"))
    #从session获取购物车
    shopping_cart = request.session.get("shopping_cart")
    #判断购物车是否存在
    if shopping_cart is None:
        #不存在，调用购物车方法
        shopping_cart = Cart()
        shopping_cart.add(book_id,amount)
        #重新将购物车存储到session
        request.session['shopping_cart']=shopping_cart
    else:
        print("dadada")
        #如果购物车存在，直接调用购物车对象的方法添加图书
        shopping_cart = shopping_cart.add(book_id,amount)
        request.session['shopping_cart']=shopping_cart
    # return render(request,'cart_app/index/car.html',{"flag":flag,"user_name":user_name,"shopping_cart":shopping_cart})
    return  HttpResponse("1")

def modify_Cart(request):
    #收集参数
    # 获取书籍的id
    book_id = int(request.GET.get("book_id"))
    # 获取书籍的数量
    amount = int(request.GET.get("amount"))
    print(amount)
    # 从session获取购物车
    shopping_cart = request.session.get("shopping_cart")
    #调用购物车方法删除
    shopping_cart2 = shopping_cart.modify(book_id, amount)
    request.session['shopping_cart'] = shopping_cart2
    # print(shopping_cart2.total_price,shopping_cart2.save_price)
    return JsonResponse({"total_price":shopping_cart2.total_price,"save_price":shopping_cart2.save_price})




