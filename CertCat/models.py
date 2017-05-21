from django.db import models
from django.utils.timezone import now
from datetime import datetime


class cert_subj(models.Model):
    OU = models.CharField(max_length=1000, verbose_name=u'OU', null=True, blank=True)
    C = models.CharField(max_length=1000, verbose_name=u'C', null=True, blank=True)
    CN = models.CharField(max_length=1000, verbose_name=u'CN', null=True, blank=True)
    O = models.CharField(max_length=1000, verbose_name=u'O', null=True, blank=True)
    L = models.CharField(max_length=1000, verbose_name=u'L', null=True, blank=True)
    ST = models.CharField(max_length=1000, verbose_name=u'ST', null=True, blank=True)
    CN = models.CharField(max_length=1000, verbose_name=u'CN', null=True, blank=True)
    street = models.CharField(max_length=1000, verbose_name=u'street', null=True, blank=True)
    title = models.CharField(max_length=1000, verbose_name=u'title', null=True, blank=True)
    emailAddress = models.CharField(max_length=1000, verbose_name=u'email', null=True, blank=True)
    serial = models.CharField(max_length=1000, verbose_name=u'serial', null=True, blank=True)
    notafter = models.DateTimeField(verbose_name=u'not after', null=True, blank=True)
    notbefore = models.DateTimeField(verbose_name=u'not before', null=True, blank=True)
    dt_update = models.DateTimeField(verbose_name=u'update date', auto_now=True)
    dt_create = models.DateTimeField(verbose_name=u'create date', auto_now_add=True)