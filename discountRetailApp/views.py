#encoding:utf-8

from django.shortcuts import render
from models import  sellerInfo,waresInfo,categoryInfo,orderInfo,consumerInfo
from django.http  import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from utils import constant
from discountRetail.settings import BASE_DIR
from PIL import Image
from os import path as fpath
# Create your views here.

# def base(request):
#     return render(request, 'discountRetailApp/base.html', {'tstring': '测试字符串'})
#
# def index(request):
#     # return HttpResponse('this is a test page')
#     contentList = ['1','2','3','4','5','6','7']
#
#     # return render(request, 'discountRetailApp/index.html', {'tstring': '测试字符串'})
#     # return  render(request, 'discountRetailApp/index.html',{'contentList':contentList})
#     return  render(request, 'discountRetailApp/index.html',{'clist':contentList,'tstring':'这是一个字符串','request':request})
#
# def cal(request):
#     return render(request, 'discountRetailApp/add.html')
#
# def people(request):
#     people = {'name': 'caiyue', 'age': '20'}
#     return render(request, 'discountRetailApp/people.html',{'people':people})
#
# def add(request):
#     a = int(request.GET['a'])
#     b = int(request.GET['b'])
#     return HttpResponse('add sum = %d' % (a+b))
#
#
# def add2(request,a,b):
#     #add2/10/20/?c=100&d=30
#     dict = request.GET
#     c = d = 0
#     if dict.has_key('c'):
#         c = dict['c']
#     if dict.has_key('d'):
#         d = dict['d']
#     return HttpResponse('add2 sum == %d' % (int(a) + int(b) + int(c) + int(d)))
#
# def minus(request):
#     a = int(request.GET['a'])
#     b = int(request.GET['b'])
#     return HttpResponse('result = %d'%(a-b))


def index(request):
    return HttpResponse('this is the index page')

@csrf_exempt
def uploadImg(request):
    method = request.method
    imgData = request.POST.get('img',None)
    if imgData:
        return HttpResponse('upload image success' + imgData)
    else:
        return HttpResponse('upload imgage failed')

#adduser
def adduser(request):
    if request.method == 'GET':
        return render(request,'discountRetailApp/user/adduser.html',{'btntitle':'添加用户'})
    else:
        username = request.POST.get('name',None)
        uage = request.POST.get('age',None)
        utel = request.POST.get('tel',None)
        uaddress = request.POST.get('address',None)
        uintro = request.POST.get('intro',None)

        logo = request.FILES.get('logo',None)
        logoname = logo.name
        logourl = None

        if logo:
            img = Image.open(logo)
            logourl = fpath.join(constant.img_prefix,logoname)
            img.save(fpath.join(BASE_DIR,logourl))

        consumer = consumerInfo.objects.create(name=username,age=uage,address = uaddress,tel=utel,logo_url = logourl,consumer_intro=uintro, register_date=datetime.now())
        consumer.save()
        return HttpResponse('adduser success')

def checkuser(request):
    if request.method == 'GET':
        return render(request,'discountRetailApp/user/checkuser.html',{'btntitle':'查询用户'})
    else:
        username = request.POST.get('name', None)
        uage = request.POST.get('age', None)
        utel = request.POST.get('tel', None)
        uaddress = request.POST.get('address', None)
        uintro = request.POST.get('intro', None)

        ret = consumerInfo.objects.get(tel__contains= '13146623011' )

        return HttpResponse(ret)
