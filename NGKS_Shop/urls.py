"""NGKS_Shop path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path('', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.paths import include, path
    2. Add a path to pathpatterns:  path('blog/', include('blog.paths'))
"""
from django.contrib import admin
from django.conf.urls import url
from SGU.views import *
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$', login,{'template_name':'login.html'}, name='login'),
    url(r'^principal/sgu/$', sgu, name='sgu'),
    url(r'^principal/sgu/chg_pass/', chg_pass, name='chg_pass'),
    url(r'^principal/sgu/(?P<username>[A-Z,a-z,0-9]+)/detalhes', detalhes, name='detalhes'),
    url(r'^principal/sgu/cadastro_user', cadastro_user, name='cadastro_user'),
    url(r'^principal/estoque/$', estoque, name='estoque'),
    url(r'^principal/fluxo/$', fluxo, name='fluxo'),
    url(r'^principal/pedidos/$', pedidos, name='pedidos'),
    url(r'^logout/', logout, name='logout'),
    url(r'^principal/$', principal, name='principal'),
    url(r'^erro_acesso/', erro_acesso, name='erro_acesso'),
]