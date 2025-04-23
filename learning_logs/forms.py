from django import forms  #表单：负责把用户的 “快递”（数据）打包、运输，用户只需填写，无需关心运输细节。后端：负责签收快递、检查内容（审核）、决定是否入库（存数据库），这是核心逻辑，必须写代码。

from .models import Topic,Entry

class TopicForm(forms.ModelForm):  #继承
    class Meta:
        model=Topic
        fields=['text']
        labels={'text':''}

'''这段代码是用 Python 语言编写的，定义了一个名为 “TopicForm” 的表单类。这个表单类继承自 “forms.ModelForm”。在 “Meta” 类中，指定了关联的模型为 “Topic”，表单中包含的字段只有 “text”，并且将 “text” 字段的标签设置为空字符串。这意味着这个表单主要用于处理与 “Topic” 模型相关的数据，并且在表单中只显示一个名为 “text” 的输入字段，且该字段没有标签。     给前端用户一个Topic类中的text输入框,让用户不用编程就能输入这个text文本给后台'''

class EntryForm(forms.ModelForm):
    class Meta:  #“Meta” 的内部类，通常用于指定与模型相关的一些元数据信息，比如关联的模型、要包含或排除的字段等。
        model=Entry
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}  #「定制文本输入框的外观，让用户输入内容时拥有更宽敞的横向空间」
