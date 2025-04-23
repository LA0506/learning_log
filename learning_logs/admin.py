from django.contrib import admin

from .models import Topic, Entry

admin.site.register(Topic)  #注册模型，Admin 不会自动管理所有模型，只有注册过的模型才会出现在后台
admin.site.register(Entry)
# Register your models here.
'''可以把 Django 的管理网站（Admin）比作你家的「智能中控室」，而注册模型就像把家里的「电器设备（数据库表）」接入中控室 —— 这样你就能通过手机 App（Admin 界面）远程控制它们。'''