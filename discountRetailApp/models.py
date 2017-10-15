#encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from utils import constant

# Create your models here.
class   consumerInfo(models.Model):
    consumerid = models.AutoField
    name = models.CharField(max_length=constant.nameMaxLength)
    age = models.IntegerField()
    address = models.CharField(max_length=constant.addressMaxLength,default='')
    tel = models.CharField(max_length=constant.telMaxLength,default='')
    logo_url = models.CharField(max_length=constant.urlMaxLength,default='')
    consumer_intro = models.CharField(max_length=constant.introMaxLength)

    register_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class sellerInfo(models.Model):
    sellerid = models.AutoField
    sellname = models.CharField(max_length=constant.nameMaxLength)
    sellerOwnerName = models.CharField(max_length=constant.nameMaxLength)
    address = models.CharField(max_length=constant.addressMaxLength)
    tel = models.CharField(max_length=constant.telMaxLength,default='')
    seller_logo = models.CharField(max_length=constant.urlMaxLength,default='')
    seller_intro = models.CharField(max_length=constant.contentMaxLength)

    lat = models.CharField(max_length=constant.floatMaxlength)
    log = models.CharField(max_length=constant.floatMaxlength)

    commit_apply_time = models.DateTimeField()
    start_bussiness_time = models.DateTimeField(auto_now_add=True)
    close_bussiness_time = models.DateTimeField()
    isInBussiness = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class categoryInfo(models.Model):
    categoryId = models.AutoField
    categoryName = models.CharField(max_length=constant.nameMaxLength)
    categoryIntro = models.CharField(max_length=constant.contentMaxLength)


class waresInfo(models.Model):
    wareId = models.AutoField
    # ,分割多个图片
    ware_img = models.CharField(max_length=constant.urlMaxLength)
   #，分割多个视频
    ware_video_url = models.CharField(max_length=constant.urlMaxLength)
    wareIntro = models.CharField(max_length=constant.contentMaxLength)
    warePrice = models.CharField(max_length= constant.priceMaxlength)

    sellerId = models.IntegerField()

    on_sail_time = models.DateTimeField(auto_now_add=True)
    init_sail_count = models.IntegerField(default=0)
    current_available_count = models.IntegerField(default=0)
    wareCategoryId = models.IntegerField()


class orderInfo(models.Model):
    order_create_time = models.DateTimeField(auto_now_add=True)

    #支付时间
    orer_complete_time = models.DateTimeField()

    #支付关闭时间,商家关闭或者成交后30天后
    order_close_time = models.DateTimeField()

    consumerid = models.IntegerField()
    sellerid = models.IntegerField()

    wareid = models.IntegerField()
    order_price = models.CharField(max_length=constant.priceMaxlength)

    order_comment = models.CharField(max_length=constant.contentMaxLength)