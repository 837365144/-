import traceback
from datetime import datetime

from copy import deepcopy

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.


#点击结算判断是否登录跳转地址
from cart_app.cart import Cart
from order_app.models import Address, Order, Orderiterm
from user_app.models import User


def order_page(request):
    # 获取用户登录状态
    flag = request.GET.get("flag")
    #获取用户id
    user_id = request.GET.get("user_id")
    if flag == "1":
        user = User.objects.filter(id = user_id)
        address = Address.objects.filter(user_id = user_id)
        print(address)
        # 先从session获取到购物车
        shopping_cart = request.session.get("shopping_cart")
        shopping_cart2 = deepcopy(shopping_cart)
        request.session["shopping_cart2"]=shopping_cart2
        shopping_cart2 = request.session.get("shopping_cart2")
        return render(request, 'order_app/order/indent.html',{"user":user,"address":address,"shopping_cart":shopping_cart2,"flag":flag,})
    else:
        return redirect('user:login:page')


#修改购车2
def modify_Cart_2(request):
    #收集参数
    # 获取书籍的id
    book_id = int(request.GET.get("book_id"))
    # 获取书籍的数量
    amount = int(request.GET.get("amount"))
    print(amount)
    # 从session获取购物车
    shopping_cart = request.session.get("shopping_cart2")
    #调用购物车方法删除
    shopping_cart2 = shopping_cart.modify(book_id, amount)
    request.session['shopping_cart2'] = shopping_cart2
    # print(shopping_cart2.total_price,shopping_cart2.save_price)
    return JsonResponse({"total_price":shopping_cart2.total_price,"save_price":shopping_cart2.save_price})


#地址存入购物车
def address_logic(request):
    # try:
    address = request.POST.get("have_address")
    # print(address)
    # 获取用户id
    user_id = request.GET.get("user_id")
    user = User.objects.get(pk=user_id)
    #获取用户登录状态和用户昵称
    flag = request.GET.get("flag")
    user_name = request.GET.get("user_name")
    # print(user_name)
    # print(shopping_cart2)
    if flag:
        if  address == "1":
            name = request.POST.get("consignee")
            detail_address1 = request.POST.get("country_id")
            detail_address2 = request.POST.get("province_id")
            detail_address3 = request.POST.get("city_id")
            detail_address4 = request.POST.get("town_id")
            detail_address5 = request.POST.get("detailed_address")
            zipcode = request.POST.get("postal_code")
            addr_mobile = request.POST.get("phone")
            telphone = request.POST.get("fixed_line_telephone")
            #存入地址
            # with transaction.atomic():
            Address(name=name,detail_address=detail_address1+','+detail_address2+','+detail_address3+','+detail_address4+','+detail_address5,zipcode=zipcode,telphone=telphone,addr_mobile=addr_mobile,user_id=user).save()
            # 从购物车获取订单
            shopping_cart2 = request.session.get("shopping_cart2")
            # 获取地址对象
            order_addrid = Address.objects.all()
            # print(order_addrid)
            order_addrid_1 = order_addrid[len(order_addrid) - 1]
            # 生成订单，存入订单
            Order(create_date=datetime.now(), price=shopping_cart2.total_price, order_addrid=order_addrid_1,order_uid=user).save()
            # 生成订单项
            # 获取订单对象
            order = Order.objects.all()
            order_1 = order[len(order) - 1]
            for i in shopping_cart2.cartltems:
                Orderiterm(shop_bookid=i.book, shop_ordid=order_1, shop_num=i.amount).save()
            orderiterm = Orderiterm.objects.filter(shop_ordid=order_1.id)
            orderiterm_amount = len(orderiterm)
            address = Address.objects.filter(order__order_addrid=order_1.order_addrid)
            return render(request, "order_app/order_close/indent ok.html",{"flag": flag, "user_name": user_name,'order_1':order_1, 'orderiterm_amount': orderiterm_amount,"address":address})
        else:
            # 获取地址对象
            address_j = address.split(',')[9]
            order_addrid = Address.objects.get(pk=address_j)
            # 从购物车获取订单
            shopping_cart2 = request.session.get("shopping_cart2")
            # print(order_addrid)
            # 生成订单，存入订单
            Order(create_date=datetime.now(), price=shopping_cart2.total_price, order_addrid=order_addrid,
                  order_uid=user).save()
            # 生成订单项
            # 获取订单对象
            order = Order.objects.all()
            order_1 = order[len(order) - 1]
            for i in shopping_cart2.cartltems:
                Orderiterm(shop_bookid=i.book, shop_ordid=order_1, shop_num=i.amount).save()
            orderiterm = Orderiterm.objects.filter(shop_ordid=order_1.id)
            orderiterm_amount = len(orderiterm)
            print(orderiterm_amount)
            address = Address.objects.filter(order__order_addrid=order_1.order_addrid)
            return render(request,"order_app/order_close/indent ok.html",{"flag":flag,"user_name":user_name,'order_1':order_1,'orderiterm_amount':orderiterm_amount,"address":address})
    else:
        return render(request,"")
# #跳转订单成功页面
# def order_ok(request):
#
#     # 获取订单对象
#     order = Order.objects.all()
#     order_1 = order[len(order) - 1]
#
#
#     return render(request,'order_app/order_close/indent ok.html',{})
