from django.db import models
from django.utils.timezone import now
from django_summernote.fields import SummernoteTextField

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'  # 指定后台显示模型名称
        verbose_name_plural = '用户列表'  # 指定后台显示模型复数名称


# ---------------------------------博客文章标签---------------------------------------
class Author(models.Model):
    name = models.CharField(verbose_name='作者名', max_length=64)

    # 使对象在后台显示更友好
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '作者名称'  # 指定后台显示模型名称
        verbose_name_plural = '作者列表'  # 指定后台显示模型复数名称
        db_table = "author"  # 数据库表名


# ---------------------------------博客文章---------------------------------------
class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    # content = models.TextField(verbose_name='正文', blank=True, null=True)
    content = SummernoteTextField(null=True)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    author = models.ForeignKey(Author, verbose_name='作者列表', on_delete=models.CASCADE, blank=False, default=1)

    # 使对象在后台显示更友好
    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ['-created_time']  # 按文章创建日期降序
        verbose_name = '文章'  # 指定后台显示模型名称
        verbose_name_plural = '文章列表'  # 指定后台显示模型复数名称
        db_table = 'article'  # 数据库表名
        get_latest_by = 'created_time'



