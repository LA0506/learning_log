'''定义learning_logs的URL模式'''

from django.urls import path  #这个函数通常用于定义 URL 模式与视图函数之间的映射关系，以实现不同的 URL 对应不同的视图处理逻辑。例如，可以使用 “path ('home/', home_view)” 来定义当访问 “/home/” 这个 URL 时，由 “home_view” 函数来处理对应的请求。
#path 来处理你输入的不同url,所展示的页面
from . import views

app_name='learning_logs'
urlpatterns=[
    #主页
    path('',views.index,name='index'),  #空值等效于/     见上由views.py中的index函数来处理该url   指定这个URL模式的名称为index,后续能够使用这个url模式索引这个localhost:8000/
    #显示所有主题的页面
    path('topics/',views.topics,name='topics'),
    #显示特定主题的详细页面
    path('topics/<int:topic_id>/',views.topic,name='topic'),  #/  /中匹配到的整数赋值给topic_id,进而在views.topic中传入topic_id  #int:可以捕捉数据库中创建实例时产生的id,然后将topics/n与views中topic关联(传入参数topic_id)
    #用于添加新主题的页面
    path('new_topic/',views.new_topic,name='new_topic'),
    #用于添加新条目的页面
    path('new_entry/<int:topic_id>',views.new_entry,name='new_entry'),
    #用于编辑条目的页面
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]