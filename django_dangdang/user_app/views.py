import os
import random
import string
import traceback

from django.db import transaction
from django.shortcuts import render, redirect,HttpResponse
from user_app import utils
# Create your views here.

from user_app.captcha.image import ImageCaptcha
from user_app.models import User

#跳转注册页面
def register_page(request):
    return render(request,"user_app/register/register.html")

#异步验证手机号
def ajax_username(request):
    username = request.POST.get("username")
    if len(username) != 11:
        return HttpResponse("0")
    elif User.objects.filter(user_email=username):
        return HttpResponse("2")
    else:
        return HttpResponse("1")

#异步验证注册验证码
def ajax_captcha(request):
    '''
    接收ajax请求
    :param request:
    :return:
    '''

    #1.获取真实的码
    realcode = request.session.get("code")
    print(realcode)
    #2.获取用户输入码
    usercode = request.POST.get("usercode")
    print(usercode)
    #判断验证码
    if realcode.lower() == usercode.lower():
        return HttpResponse("1")
    else:
        return HttpResponse("0")




#注册接收跳转页面
def register_logic(request):
    try:
        #获取用户输入的邮箱/手机号码
        username = request.POST.get("txt_username")
        #获取用户输入的第一次密码
        password1 = request.POST.get("txt_password")
        #获取用户输入的第二次密码
        password2 = request.POST.get("txt_repassword")
        salt = utils.getSalt()
        password = utils.hashCode(password2,salt=salt)
        #获取真实的验证码
        realcode = request.session.get("code")
        #获取用户输入的验证码
        usercode = request.POST.get("txt_vcode")
        with transaction.atomic():
            if realcode.lower() == usercode.lower() :
                print("hello")
                if password1 == password2:
                    print("hello111")
                    User(user_email=username,user_password=password,salt=salt).save()
                    user = User.objects.filter(user_email=username)
                    print("lala")
                    return render(request,"user_app/register/register ok.html",{"user":user})
                else:
                    return redirect("user:register:page")
            else:
                return redirect("user:register:page")
    except:
        traceback.print_exc()
        #注册失败重新回到注册页面
        return redirect("user:register:page")


# #跳转注册成功页面
# def register_ok(request):
#     return render(request,"user_app/register/register ok.html")

#生成验证码
def get_captcha(request):
    #1.创建一个ImageCaptcha对象
    cap = ImageCaptcha(fonts=[os.path.abspath("captcha/font/simhei.ttf")])
    #获取4位随机验证码值
    code_list = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4)
    code = ''.join(code_list)
    #3.将验证码存入session
    request.session["code"]=code
    print(code)
    #4.生成验证码图片
    data = cap.generate(code)
    #5.写出图片
    return HttpResponse(data,"image/png")

#跳转登录页面
def login_page(request):
    return render(request,"user_app/login/login.html")

#异步登录接收页面
def ajax_login_logic(request):
    username = request.POST.get("username")
    password = request.POST.get('password')
    database_user = User.objects.filter(user_email=username)
    if database_user:
        database_password = database_user[0].user_password
        salt = database_user[0].salt
        password1 = utils.hashCode(password,salt=salt)
        password_1 = password1
        if database_password == password_1:
            print("haha")
            return HttpResponse("1")
        else:
            print("hheihei")
            return HttpResponse("0")
    else:
        return HttpResponse("0")

#异步验证登录验证码
def ajax_captcha_login(request):
    '''
    接收ajax请求
    :param request:
    :return:
    '''

    #1.获取真实的码
    realcode = request.session.get("code")
    print(realcode)
    #2.获取用户输入码
    usercode = request.POST.get("usercode")
    print(usercode)
    #判断验证码
    if realcode.lower() == usercode.lower():
        return HttpResponse("1")
    else:
        return HttpResponse("0")

