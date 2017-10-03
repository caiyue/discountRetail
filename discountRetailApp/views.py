#encoding:utf-8

from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

def base(request):
    return render(request, 'discountRetailApp/base.html', {'tstring': '测试字符串'})

def index(request):
    # return HttpResponse('this is a test page')
    contentList = ['1','2','3','4','5','6','7']

    # return render(request, 'discountRetailApp/index.html', {'tstring': '测试字符串'})
    # return  render(request, 'discountRetailApp/index.html',{'contentList':contentList})
    return  render(request, 'discountRetailApp/index.html',{'clist':contentList,'tstring':'这是一个字符串','request':request})

def cal(request):
    return render(request, 'discountRetailApp/add.html')

def people(request):
    people = {'name': 'caiyue', 'age': '20'}
    return render(request, 'discountRetailApp/people.html',{'people':people})

def add(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    return HttpResponse('add sum = %d' % (a+b))


def add2(request,a,b):
    #add2/10/20/?c=100&d=30
    dict = request.GET
    c = d = 0
    if dict.has_key('c'):
        c = dict['c']
    if dict.has_key('d'):
        d = dict['d']
    return HttpResponse('add2 sum == %d' % (int(a) + int(b) + int(c) + int(d)))

def minus(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    return HttpResponse('result = %d'%(a-b))

