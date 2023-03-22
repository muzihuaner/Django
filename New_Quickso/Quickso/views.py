from plistlib import Data

from django.shortcuts import render, HttpResponse
from Quickso.models import Category, Links


# Create your views here.

def index(request):
    CategoryList = Category.objects.all()
    DataList = []
    if CategoryList:
        for category in CategoryList:
            DataList = Links.objects.filter(category=category)
    return render(request, 'index.html', {'CategoryList': CategoryList, 'link': DataList})


def page_not_found(request, exception):
    return render(request, '404.html')


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("user")
    password = request.POST.get("password")
    if username == 'admin' and password == 'admin':
        return render(request, "login.html")
        # return HttpResponse("登录成功！")

    else:
        # return HttpResponse("登录失败！")
        return render(request, "login.html", {"error_msg": "登录失败，请检查用户名和密码！"})
