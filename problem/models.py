# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class problem_solve(models.Model):
    enrol=models.CharField(max_length=15,default='161B071')
    solution=models.TextField()
    correct=models.BooleanField(default='False')
    time=models.IntegerField(default=0)

    
    

