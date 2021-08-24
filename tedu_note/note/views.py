from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from note.models import Note


# {{ 变量 }}：变量代码
# {% 代码段落 %}：逻辑代码

def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            # 检查Cookies
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                # 回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid

        return fn(request, *args, **kwargs)

    return wrap


@check_login  # 装饰器：判断是否登录
def add_note(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        # 处理数据
        uid = request.session['uid']
        title = request.POST['title']
        content = request.POST['content']

        Note.objects.create(title=title, content=content, user_id=uid)
        return HttpResponse('添加笔记成功')


def all_note(request):
    all_note = Note.objects.filter(is_active=True)
    return render(request, 'note/all_note.html', locals())


def update_note(request, note_id):
    """修改笔记"""
    try:
        # 查
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        print('update note error is %s' % e)
        return HttpResponse('--The note is note existed')

    if request.method == 'GET':
        return render(request, 'note/update_note.html', locals())
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        # 改
        note.title = title
        # 保存
        note.save()
        return HttpResponseRedirect('/note/all_note')

def delete_note(request):
    # 通过获取查询字符串 note_id拿到要删除的note的id
    note_id = request.GET.get('note_id')
    if not note_id:
        return HttpResponse('---请求异常')
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        print('---delete note get error %s' % (e))
        return HttpResponse('---The note id is error')
    # 将其is_active改成False
    note.is_active = False
    note.save()
    # 302跳转至all_book
    return HttpResponseRedirect('/note/all_note')
