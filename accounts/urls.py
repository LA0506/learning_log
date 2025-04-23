'''为应用程序accounts定义URL模式'''

from django.urls import path,include
from . import views

app_name='accounts'
urlpatterns=[
    #包含默认的身份验证URL
    path('',include('django.contrib.auth.urls')),  # +django内置认证路径例如login,因此这个url即为登录页面
    path('register/',views.register,name='register')
]

