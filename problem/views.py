# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django import forms
from .forms import ans
from .models import problem_solve
from .utils import work
import subprocess


def question(request):
    return render(request,'question.html')
def home(request):
    return render(request,'home.html')

def answer(request,num="1"):
    form=ans(request.POST)
    context={
        'form':form
    }
    if request.method=='POST':
        if form.is_valid():
            solution=form.cleaned_data['Solution']
            print(solution)
            object = problem_solve()
            enrol=form.cleaned_data['Enrollment']
            print(enrol)
            r=work(solution)
            object.solution=solution
            object.enrol=enrol
            if r!=0:
                object.correct=False
                object.save()
                return HttpResponse('Wrong Answer OR Compilation Error!!! <br> Please Check your Code...')
            else:
                linux='a.exe<in_'+num+'.txt>output'+num+'.txt'
                linux='start 1s.bat & '+linux
                print(linux)
                k=subprocess.call(linux,shell=True)
                if k==0:
                    f1 = open("result" + num + ".txt", "r")
                    f1_data = f1.readlines()
                    f2 = open("output" + num + ".txt", "r")
                    f2_data = f2.readlines()
                    print(f1_data)
                    print(f2_data)
                    if f1_data==f2_data:
                        object.correct = True
                        object.save()
                        return HttpResponse("Accepted")
                    else:
                        object.save()
                        return HttpResponse("Wrong Answer")
                else:
                    object.save()
                    return HttpResponse("Wrong Answer")
            object.save()
    return render(request,'answer.html',context)
