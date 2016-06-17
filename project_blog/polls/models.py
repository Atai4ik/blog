# coding: utf-8

from __future__ import unicode_literals

import datetime
from django.utils import timezone
from django.db import models

class Poll(models.Model):
    question = models.CharField(u'Вопрос', max_length=200)
    pub_date = models.DateTimeField('дата публикации')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        verbose_name = u'голосование'
        verbose_name_plural = u'голосования'

    def __unicode__(self):
        return "%s " % (self.question)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(u'Выбор', max_length=200)
    vote = models.IntegerField(u'голос')

    class Meta:
        verbose_name = u'выбор'
        verbose_name_plural = u'выборы'

    def __unicode__(self):
        return "%s " % (self.choice)