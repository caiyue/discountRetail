from __future__ import unicode_literals

from django.db import models

# Create your models here.

class   Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name

class   Blog(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    def __unicode__(self):
        return self.name

class   Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField()
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField()
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):
        return self.headline

