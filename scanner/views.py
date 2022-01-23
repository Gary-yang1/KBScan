from django.shortcuts import render
from django.http import HttpResponse
from . import models
from scanner.tools import StrToList
from scanner.tools import CheckKB


# Create your views here.

def index(request):
    """
    视图函数，至少有一个参数
    :param request: 接受请求对象，类型为HttpRequest
    :return: 返回响应对象，类型：HttpResponse
    """
    return render(request, 'scanner/index.html')


def result(request):
    if request.method == 'POST':
        KBNum_str = request.POST['KBNum']
        Str_list = StrToList.toList(KBNum_str)  # 获取漏洞编号，存在list中
        reslist = CheckKB.check(Str_list)
        return HttpResponse("缺少的补丁有：" + str(reslist))
    else:
        return HttpResponse('error')
