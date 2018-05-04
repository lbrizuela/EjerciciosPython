'''
Created on 4 may. 2018

@author: lbrizuela
'''
from django.shortcuts import render


def inicio(request):
    return render(request, 'paginaInicio.html')