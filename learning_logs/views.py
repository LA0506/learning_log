from django.shortcuts import render,redirect  #“render” 函数通常用于将给定的模板与相应的数据结合起来，并返回一个经过渲染的 HTTP 响应对象，以便在 Django 应用程序中呈现网页内容给用户。
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# Create your views here.
def index(request):
    '''学习笔记的主页'''
    return render(request,'learning_logs/index.html')  #xxx.html为模版

@login_required  #当用户登录之后才能执行下面函数(关联url配置)
def topics(request):
    '''显示所有的主题'''
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')  #objects获得该类中的数据(在数据库中查询数据)   #增加filter(),用户登录之后request会带上用户的user集,设置每个用户只能看到自己的外键关联的主题(同时关联到条目)
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)  #将context传入该模版,该模板再使用这些数据渲染或生成内容

@login_required
def topic(request,topic_id):
    '''显示单个主题及其所有的条目'''
    topic=Topic.objects.get(id=topic_id)  #获得特定的主题对象
    #确认请求的主题属于当前用户
    if topic.owner!=request.user:  #防止直接从特定主题url查看个人数据
        raise Http404
    entries=topic.entry_set.order_by('-date_added') #使用外键关联获取对应数据
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method!='POST':
        #未提交数据:创建一个新表单
        form=TopicForm()
    else:
        #POST提交的数据:对数据进行处理
        form=TopicForm(data=request.POST)  #传入的POST请求传入TopicForm类(在forms中创建的类)中创建实例form
        if form.is_valid():  #如果表单数据是合法的
            new_topic=form.save(commit=False)
            new_topic.owner=request.user  #现在创建新主题需要与owner外键关联否则关联不了
            new_topic.save()  #创建新主题,写入数据库
            return redirect('learn_logs:topics')  #保存后重定向页面(跳转页面)
        #显示空表单或指出表单数据无效
    context={'form':form}  #如果不是POST请求或者请求不合法,创建字典传入new_topic页面
    return render(request,'learning_logs/new_topic.html',context)  #如果用户点击该url,由于没有传入任何数据,直接进入该页面,创建新主题之后跳转到topics页面

@login_required
def new_entry(request,topic_id):
    '''在特定的主题中添加新条目'''
    topic=Topic.objects.get(id=topic_id)  #获得主题

    if request.method!='POST':
        #未提交数据:创建一个空表单
        form=EntryForm()
    else:
        #POST提交的数据:对数据进行处理
        form=EntryForm(data=request.POST)  #不加instance就是创建新实例
        if form.is_valid():
            new_entry=form.save(commit=False)  #save创建一个新条目,但是不保存(不写入数据库)
            new_entry.topic=topic  #赋予主题(使用了Entry类中的topic属性(链接外键))
            new_entry.save()
            return redirect('learning_logs:new_entry.html',topic_id=topic_id)

    #显示空表单或指出表单数据无效
    context={'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    '''编辑既有的条目'''
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    #防止
    if topic.owner!=request.user:
        raise Http404

    if request.method!='POST':
        #初次请求:使用条目充填表单
        form=EntryForm(instance=entry)  #初次点击进入编辑页面,展示原来的条目
    else:
        #POST提交的数据:对数据进行处理
        form=EntryForm(instance=entry,data=request.POST)  #初始化：基于 instance 的原始数据渲染表单。接收新值：用 data 的值覆盖用户修改的字段（如用户只改了标题，其他字段保留 instance 的值）。验证与保存：验证通过后，form.save() 会更新数据库中的 instance 记录，而非创建新对象。
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)  #与new_entry里的区别,这里的topic.id是本方法获取的变量,是反向通过条目获得主题,再获得主题id,修改完成回到条目页面
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)

