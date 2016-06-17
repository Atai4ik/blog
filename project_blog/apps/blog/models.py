# coding: utf-8

from django.db import models

class News(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    author = models.CharField(u'Автор', max_length=40)
    text = models.TextField(u'Текст')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'

    def __unicode__(self):
        return "%s / %s" % (self.title, self.author)
