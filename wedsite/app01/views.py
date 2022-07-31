import os

import cv2

from app01 import methods
from app01 import methods2
from django.db.models import Model
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
from app01 import models


# media_path = ''


def index(request):
    return HttpResponse('欢迎使用Django')


def index_add(request):
    return HttpResponse("你到底想怎么样！")


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    name = ["庄达菲", "陈昊宇", "李庚希"]
    return render(request, 'tpl.html', {"n1": name})


def news(request):
    import requests
    res = requests.get("https://www.bing.com")
    data_list = res.json()
    print(data_list)
    print('ok')
    return render(request, 'news.html', {"data_list": data_list})


def twitter(request):  # 这一节学习，有请求必然要响应
    print(request.method)
    # 获取请求方式，可能是下面两种的任何一种

    print(request.GET)
    # 明面上传参数
    print(request.POST)
    # 请求体，偷偷的。
    # return HttpResponse('LoveLive!Superstar!')#这是响应的一种的、方式
    # return render(request,'xxx.html',{"whatever":whateverJson())
    # 这也是回复响应的一种方式，给他一个html页面
    return redirect("https://twitter.com/home")


def login(req):
    if req.method == 'GET':
        print(req.method)
        return render(req, "login.html")
    else:
        print(req.method)
        print(req.FILES)
        file = req.FILES.get('avatar')

        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, file.name)
        f = open(media_path, mode='wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        # image_code(media_path)
        return render(req, 'login.html')


#
# from io import BytesIO
#
#
# def image_code(media_path):
#     img = Image.open(media_path)
#     stream = BytesIO()
#     img.save(stream, 'png')
#     return HttpResponse(stream.getvalue())


def upload(request):
    if request.method == 'GET':
        print(request.method)
        path = 'img/you.jpg'
        return render(request, "upload.html", {"path": path})
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)
        #
        img = methods.robs(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
        # return render(request, 'upload.html', {'path': path})


def navigate(re):
    if re.method == 'GET':
        return render(re, 'navigate.html')


def borrow(request):
    if request.method == 'GET':
        return render(request, 'borrow.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)
        #
        img = methods.robs(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response

    return render(request, 'borrow.html')


def _and(request):
    if request.method == 'GET':
        return render(request, '_and.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        avatar2 = request.FILES.get('avatar2')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        media_path2 = os.path.join(settings.MEDIA_ROOT, avatar2.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        f2 = open(media_path2, mode='wb')
        for chunk in avatar2.chunks():
            f2.write(chunk)
        f2.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)

        img = methods.and_operation(media_path, media_path2)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response

    return render(request, '_and.html')


def _or(request):
    if request.method == 'GET':
        return render(request, '_or.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        avatar2 = request.FILES.get('avatar2')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        media_path2 = os.path.join(settings.MEDIA_ROOT, avatar2.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        f2 = open(media_path2, mode='wb')
        for chunk in avatar2.chunks():
            f2.write(chunk)
        f2.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)

        img = methods.or_operation(media_path, media_path2)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, '_or.html')


def _not(request):
    if request.method == 'GET':
        return render(request, '_not.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)
        #
        img = methods.not_operation(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response

    return render(request, '_not.html')


def ope_add(request):
    if request.method == 'GET':
        return render(request, 'ope_add.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        avatar2 = request.FILES.get('avatar2')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        media_path2 = os.path.join(settings.MEDIA_ROOT, avatar2.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        f2 = open(media_path2, mode='wb')
        for chunk in avatar2.chunks():
            f2.write(chunk)
        f2.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)

        img = methods.ope_add(media_path, media_path2)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'ope_add.html')


def ope_subtract(request):
    if request.method == 'GET':
        return render(request, 'ope_subtract.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        avatar2 = request.FILES.get('avatar2')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        media_path2 = os.path.join(settings.MEDIA_ROOT, avatar2.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        f2 = open(media_path2, mode='wb')
        for chunk in avatar2.chunks():
            f2.write(chunk)
        f2.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)

        img = methods.ope_subtract(media_path, media_path2)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'ope_subtract.html')


def ope_multiply(request):
    if request.method == 'GET':
        return render(request, 'ope_multiply.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        avatar2 = request.FILES.get('avatar2')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        media_path2 = os.path.join(settings.MEDIA_ROOT, avatar2.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        f2 = open(media_path2, mode='wb')
        for chunk in avatar2.chunks():
            f2.write(chunk)
        f2.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)

        img = methods.ope_multiply(media_path, media_path2)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'ope_multiply.html')


def ope_divide(request):
    if request.method == 'GET':
        return render(request, 'ope_divide.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        avatar2 = request.FILES.get('avatar2')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        media_path2 = os.path.join(settings.MEDIA_ROOT, avatar2.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        f2 = open(media_path2, mode='wb')
        for chunk in avatar2.chunks():
            f2.write(chunk)
        f2.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)

        img = methods.ope_divide(media_path, media_path2)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'ope_divide.html')


def flip(request):
    if request.method == 'GET':
        return render(request, 'flip.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)
        #
        img = methods.Flip(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'flip.html')


def affine_trans(request):
    if request.method == 'GET':
        return render(request, 'affine_trans.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)
        #
        img = methods.affine_trans(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'affine_trans.html')


def erosion(request):
    if request.method == 'GET':
        return render(request, 'erosion.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)
        #
        img = methods.erosion(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'erosion.html')


def dilation(request):
    if request.method == 'GET':
        return render(request, 'dilation.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        # with open(avatar.name, 'wb') as f:
        #     for line in avatar:
        #         f.writ4re(line)
        #
        img = methods.dilation(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'dilation.html')


def morph_open(request):
    if request.method == 'GET':
        return render(request, 'morph_open.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.morph_open(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'morph_open.html')


def morph_close(request):
    if request.method == 'GET':
        return render(request, 'morph_close.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.morph_close(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'morph_close.html')


def neighbor_aver(request):
    if request.method == 'GET':
        return render(request, 'neighbor_aver.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.neighbor_aver(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'neighbor_aver.html')


def median_filter(request):
    if request.method == 'GET':
        return render(request, 'median_filter.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.median_filter(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'median_filter.html')


def ele_roberts(request):
    if request.method == 'GET':
        return render(request, 'ele_roberts.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.roberts(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'ele_roberts.html')


def sobel(request):
    if request.method == 'GET':
        return render(request, 'sobel.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.sobel(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'sobel.html')


def prewitt(request):
    if request.method == 'GET':
        return render(request, 'prewitt.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.prewitt(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'prewitt.html')


def laplacian(request):
    if request.method == 'GET':
        return render(request, 'laplacian.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.laplacian(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'laplacian.html')


def lowpass_filter(request):
    if request.method == 'GET':
        return render(request, 'lowpass_filter.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.sort_filter(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'lowpass_filter.html')


def butterworth_low_filter(request):
    if request.method == 'GET':
        return render(request, 'butterworth_low_filter.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods2.butterworth_low_filter(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'butterworth_low_filter.html')


def highpass_filter(request):
    if request.method == 'GET':
        return render(request, 'highpass_filter.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.highpass_filter(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'highpass_filter.html')


def butterworth_high_filter(request):
    if request.method == 'GET':
        return render(request, 'butterworth_high_filter.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.butterworth_high_filter(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'butterworth_high_filter.html')


def robs(request):
    if request.method == 'GET':
        return render(request, 'robs.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.robs(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'robs.html')


def sob(request):
    if request.method == 'GET':
        return render(request, 'sob.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.sob(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'sob.html')


def lap(request):
    if request.method == 'GET':
        return render(request, 'lap.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.lap(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'lap.html')


def log(request):
    if request.method == 'GET':
        return render(request, 'log.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.log(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'log.html')


def cny(request):
    if request.method == 'GET':
        return render(request, 'cny.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.cny(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'cny.html')


def noise_desc(request):
    if request.method == 'GET':
        return render(request, 'noise_desc.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.noise_desc(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'noise_desc.html')


def aver_filter(request):
    if request.method == 'GET':
        return render(request, 'aver_filter.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.aver_filter(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'aver_filter.html')


def sort_filter(request):
    if request.method == 'GET':
        return render(request, 'sort_filter.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.sort_filter(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'sort_filter.html')


def opt_filter(request):
    if request.method == 'GET':
        return render(request, 'opt_filter.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.opt_filter(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'opt_filter.html')


def line_change(request):
    if request.method == 'GET':
        return render(request, 'line_change.html')
    elif request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')
        from django.conf import settings
        media_path = os.path.join(settings.MEDIA_ROOT, avatar.name)
        f = open(media_path, mode='wb')
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        img = methods.line_change(media_path)
        another_path = os.path.join(settings.MEDIA_ROOT, 'test' + avatar.name)
        cv2.imwrite(another_path, img)
        try:
            Model.object.create(username=name, avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}
        from django.http import FileResponse
        response = FileResponse(open(another_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename=tset.jpg"  # 注意filename不支持中文
        return response
    return render(request, 'line_change.html')
