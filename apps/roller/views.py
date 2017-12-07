# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print("you are in the roller/index method!")
    return HttpResponse("roller app index placeholder")
