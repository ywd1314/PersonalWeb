from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Article, Author
import markdown


# 登录界面
def login(request):
    return render(request, 'login.html')

# 退出登录
def logout(request):
    del request.session['IS_LOGIN']
    return render(request, 'login.html')

# 登录成功后
def afterlogin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists() == False:
            error_msg = '没有此用户'
            return render(request, 'login.html', context={'error_msg': error_msg})
        elif User.objects.filter(username=username).first().password != password:
            error_msg = '密码错误'
            return render(request, 'login.html', context={'error_msg': error_msg})
        else:
            request.session['IS_LOGIN'] = True
            request.session.set_expiry(0)
            return render(request, 'afterlog.html')
    else:
        return render(request, 'login.html')


def blog(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        article = Article.objects.all()
        return render(request, 'blog.html', context={'article_list': article})
    else:
        return render(request, 'login.html')


def detail(request, pk):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        article = Article.objects.get(id=pk)
        article.content = markdown.markdown(article.content,
            extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
           ])
        context = {'article': article}
        return render(request, 'work.html', context=context)
    else:
        return render(request, 'login.html')


