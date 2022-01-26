## 用Django写一个简易的漫画网站

玩爬虫的时候，喜欢用它来爬漫画。漫画爬到手了，但是没有分类，找起来挺麻烦的，阅读体验感也不好，于是就想写一个简单的漫画网站

### 一些唠叨

**为什么要写漫画网站，为什么不用管理漫画的软件**

想写漫画网站主要还是想通过一个开发的过程去了解它们是怎么做到业务处理与交互的。用实践的方式搞清楚一些原理与逻辑。目前还在学习阶段，使用漫画管理软件不利于提升自己的~~学习能力~~。再说这个项目也是拿来练练手的哈哈哈。

### 相关技术

* 前端框架：Bootstrap
* web框架：Django
* 数据库：MySQL

**运行环境与工具**

* 编译器： pycharm
* python3.8

这个项目没有采用前后端分离的方式，所以真的是简单漫画网站

### 网站功能

* 瀑布式阅读
* 搜索
* 分类
* 目录
* 后台管理

效果图如下（界面也非常简单）

首页：

![image-20220125211809141.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c646a7fd978448258f0a038b9bd3e82a~tplv-k3u1fbpfcp-watermark.image?)

漫画详情页：

![image-20220125212621728.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10905622fec2460c9bedea831f99fd86~tplv-k3u1fbpfcp-watermark.image?)

搜索：

![image-20220125213027524.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81742366614f4c91aa290247ee03b7fa~tplv-k3u1fbpfcp-watermark.image?)

搜索结果：

![image-20220125213015541.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66537ba525054ec695cecec1362603ac~tplv-k3u1fbpfcp-watermark.image?)

漫画内容：

![image-20220125213648034.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c752db9be3294d158b8e65374535f0e1~tplv-k3u1fbpfcp-watermark.image?)

后台管理：

![image-20220125221956622.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/403ce7d852af401e9ec7e4f9899168db~tplv-k3u1fbpfcp-watermark.image?)

分类管理：

![image-20220125222046426.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ed1a8c9d25d49169d8f2bf9f20be22f~tplv-k3u1fbpfcp-watermark.image?)

![image-20220125222111124.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13f004779864bbd9110fcca7c6a7eda~tplv-k3u1fbpfcp-watermark.image?)

章节管理：

![image-20220125222314610.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a43487b1154488fbb7b5663760549af~tplv-k3u1fbpfcp-watermark.image?)

![image-20220125222259828.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/842c7d14412d4db09eb0e2b61768368c~tplv-k3u1fbpfcp-watermark.image?)

### 项目详情

#### 目录结构

```shell
comicweb
 │  manage.py
 ├─comic
 │  │  admin.py
 │  │  apps.py
 │  │  models.py
 │  │  tests.py
 │  │  urls.py
 │  │  views.py
 │  ├─static
 │  │  └─comic
 │  │      ├─css
 │  │      ├─fonts
 │  │      └─js
 ├─comicweb
 │  │  asgi.py
 │  │  settings.py
 │  │  urls.py
 │  │  wsgi.py
 └─templates
    │  base.html
    └─comic
        │   category_list.html
        │   chapter_src.html
        │   comic_chapter_list.html
        │   errors.html
        │   index.html
        │   results.html

```

#### 数据关系模型

![image-20220125163146485.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bd18192cf3f4d00875dad7ec2c9eb3f~tplv-k3u1fbpfcp-watermark.image?)

#### 配置settings.py

没有使用django自带的sqlite3数据库，使用外连的数据库，需要做以下的配置

comicweb/comicweb/settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',		#数据库名
        'HOST': '',		#本地写127.0.0.1，服务器就写ip
        'PORT':'3306',	#MySQl端口
        'USER':'',		#用户名
        'PASSWORD':''	#密码
    }
}
```

Django有自带的后台管理，但是界面太丑了，所以我这里使用的是simpleui这个插件，先安装再配置

安装：

```python
pip install django-simpleui
```

配置：

```python
INSTALLED_APPS = [
    'simpleui',
]
```

登录后台的时候，记得先注册超级用户

#### 注册Admin

* comicweb/comic/apps.py

```python
class ComicConfig(AppConfig):
    name = 'comic'
    verbose_name = '漫画管理'
```

* comicweb/comic/admin.py

分别注册漫画管理，分类管理，章节管理类

```python
from .models import Comic, Category, Charter

admin.site.site_header = '后台'  # 设置header
admin.site.site_title = '管理后台'   # 设置title
admin.site.index_title = '管理'

class ComicAdmin(admin.ModelAdmin):
    list_display = ['comic_id', 'comic_name', 'category', 'author', 'context', 'pictures']
    fields = ['comic_id', 'comic_name', 'category', 'author', 'context', 'pictures']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']

class CharterAdmin(admin.ModelAdmin):
    list_display = ['charter_id', 'charter_name', 'comic_id']
admin.site.register(Comic, ComicAdmin)
admin.site.register(Charter, CharterAdmin)
admin.site.register(Category, CategoryAdmin)
```

#### 路由

```python
# comicweb/comic/urls.py
app_name = 'comic'
urlpatterns = [
    path('',views.Index,name='index'),
    path('comic/<int:comic_pk>',views.comic_chapter,name='comic_chapter_list'),
    path('chapter/<int:charter_pk>',views.chapter_src,name='chapter_src'),
    path('search/',views.search,name='search'),
    path('category/<int:pk>',views.category,name='category_list'),
]
```

网站包括5个路由

``pk可以理解为id``

* /  : 网站首页
* /comic/:comic_pk : 漫画详情页面
* /chapter/:charter_pk : 漫画章节详情页面
* /search:  搜索页面
* /category/:pk  :分类页面

#### 视图

* 搜索模块

```python
def search(requset):
    q = requset.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(requset,'comic/errors.html',{'error_msg':error_msg})
    comic_list = Comic.objects.filter(comic_name__icontains=q)
    return render(requset,'comic/results.html',{'error_msg':error_msg,
                                                'comic_list':comic_list})
```

* 分类模块

```python
def category(request,pk):    categories = Category.objects.get(id=pk)    category_comics = categories.comic_set.all()    return render(request,'comic/category_list.html',context={'categories':categories,'category_comics':category_comics})
```

* 漫画章节模块

```python
def comic_chapter(request,comic_pk):    comic_details = Comic.objects.get(comic_id=comic_pk)    comic_chapters = comic_details.charter_set.all()    return render(request,'comic/comic_chapter_list.html',context={'comic_details':comic_details,'comic_chapters':comic_chapters})
```

* 章节漫画图片模块

```python
def chapter_src(request,charter_pk):    chapter_detials = Charter.objects.get(charter_id=charter_pk)    temp_src = chapter_detials.src    comic_srcs = temp_src.split(',')    return render(request,'comic/chapter_src.html',context={'comic_srcs':comic_srcs})
```

#### template模块

这一部分属于前端代码部分，我前端相关知识学的不是很好，所以写的有点乱，

这里就不赘述了，可以看项目源码

```
base.html 				# 基本页面模板，其他页面是继承该模板的基础上再写一些效果category_list.html		# 分类列表chapter_src.html		# 章节漫画图comic_chapter_list.html	# 漫画详情errors.html				# 出错提示页面index.html				# 主页面results.html			# 搜索返回结果的页面
```

### 不足的地方

这个网站真的还有很多不足的地方，也没有进行优化，分页，轮播图，详细分类面板等功能都没有开发好。后续应该会完善的！

### 声明

本网站的漫画是通过爬取其他漫画网站的漫画作为数据源，出于此原因，这里采集的漫画数据将不在开源范围内。

### 最后

把代码开源出来，只不过是想记录自己摸索整个漫画网站是怎么形成的，因为网上基本没有什么教程教怎么写漫画网站，不过参考别人的项目可以得到一些思路。Django对于小项目，确实有点小材大用了哈哈哈，至于为什么选择Django，是因为当时只会用Django这一个框架（有点偏执了）而且它自带后台。

