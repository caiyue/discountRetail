#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class   Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=100,default='暂无信息')

    def __unicode__(self):
        return self.name

class   Blog(models.Model):
    auth = models.CharField(u'作者',max_length=30,default='no author')
    email = models.EmailField(u'邮箱')
    title = models.CharField(u'标题',max_length=256,default='empty title')
    update_time = models.CharField(u'更新时间',max_length=256,default=u'暂无更新')
    content = models.TextField(u'内容',max_length=1000,default='empty content')

    def __unicode__(self):
        return self.title

class   Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=30)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):
        return self.headline


class   Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=11)

    def __unicode__(self):
        return self.name
