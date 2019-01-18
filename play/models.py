from __future__ import unicode_literals

from django.db import models


class Play(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()


class Employee(models.Model):
    name = models.CharField(max_length=64)
    position = models.CharField(max_length=16)

    # def to_json(self):
    #     fields = []
    #     for field in self._meta.fields:
    #         fields.append(field.name)
    #
    #     d = {}
    #     for attr in fields:
    #         d[attr] = getattr(self, attr)
    #
    #     import simplejson
    #     return simplejson.dumps(d)
    
    def __str__(self):
        return self.name


class Result(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.DO_NOTHING)
    first = models.IntegerField()
    second = models.IntegerField()
    third = models.IntegerField()

    def __str__(self):
        return self.employee.name
