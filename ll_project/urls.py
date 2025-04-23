"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include  #导入函数include(),为了创建对应程序learning_logs的url

urlpatterns = [  #在runserver之后,Django会自动在settings中调用项目名.urls(即本文件),查看里面的列表urlpatterns,并且后面的include('learning_logs.urls') 会导入应用的 urls.py，并合并其 urlpatterns 列表。
    path("admin/", admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('learning_logs.urls')),  #创建url  引入名为 “learning_logs.urls” 模块中的 URL 配置,将 learning_logs 应用的所有 URL 模式归入 learning_logs 命名空间,learning_logs在learning_logs.urls中命名,后续引用该应用中的url使用learning_logs:xxx进行匹配,避免名字重复带来的影响,例如两个应用中均有topic链接,不用learning_logs:topic的话会出错        前面的空值,即匹配所有的/,后面应用中的的url如topic直接加到/后面
]
