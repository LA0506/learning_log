from django.db import models
from django.contrib.auth.models import User  #引入模型User

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text=models.CharField(max_length=200)  #定义一个字符，最长200个字符
    date_added=models.DateTimeField(auto_now_add=True)  #每次创建新主题时将传入当前时间
    owner=models.ForeignKey(User,on_delete=models.CASCADE)   #将主题与用户外键关联起来,只有该用户能看见自己创建的主题(同时关联到条目),用户删除主题一起删除

    def __str__(self):  #在某些需要显示对象文本的情况下，该函数会自动执行   ***Django 在需要「对象文本表示」的场景（Admin、模板、打印）强制调用 __str__，无需手动触发。
        '''返回模型的字符串表示'''
        return self.text  #所以创建实例后，在管理网站会自动执行该函数，显示主题

class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)  #设置个变量，赋值为Topic对象的外键，将Topic（某主题）与之条目相关联，后面的设置是当对象删除，与之关联的条目一起删除    ***Admin 的默认行为：只要模型包含外键，Admin 会自动识别并生成关联选择组件，无需在 ModelAdmin 中配置 fields 或 formfield_for_foreignkey。__str__ 的关键作用：下拉框显示的内容由关联模型（Topic）的 __str__ 决定,也就是可以选择与哪个主题相关联(且主题会执行__str__()，返回字段)

    text=models.TextField()  #设置属性text，字段长度不受限制
    date_added=models.DateTimeField(auto_now_add=True)  #同上

    class Meta:
        verbose_name_plural='entries'  #Django 默认会在模型名后加 s 作为复数（如 Entry → Entrys），但 Entry 的复数应为 Entries。在 Admin 后台和日志中，正确的复数名称避免歧义。   Django 模型中的 class Meta 是一个 **「元数据配置单」，它通过 Django 的元编程机制 **（而非传统继承）为模型提供额外信息。虽然它只是一个普通的嵌套类（没有显式继承），但 Django 会约定俗成地读取其中的属性，就像你在餐厅填写「菜单备注栏」（Meta），厨师（Django）会按备注调整菜品（模型行为）。  Django 预定义了 Meta 类的合法属性（如 verbose_name_plural、ordering、db_table），这些属性会被模型元类解析，用于修改模型的行为或显示。

    def __str__(self):  #同上
        '''返回一个表示条目的简单字符串'''
        return f"{self.text[:50]}..."  #自动执行，但不会显示所有内容，截断避免长文本刷屏，省略号提示内容未完全显示。
