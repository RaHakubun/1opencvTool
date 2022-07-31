"""wedsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01 import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},name='media'),
    path('index/', views.index,name="index"),
    path('index/add',views.index_add,name="index_add"),
    path('user/list/',views.user_list,name="user_list"),
    path('user/add/',views.user_add,name="user_add"),
    path('tpl',views.tpl,name="tpl"),
    path('news/',views.news,name="news"),
    path('twitter/',views.twitter,name="twitter"),
    path('login/',views.login,name="login"),
    #path('image/code/',views.image_code,name="image_code"),
    path('navigate/',views.navigate,name="navigate"),
    re_path(r'^upload', views.upload,name='upload'),
    path('borrow/',views.borrow,name='borrow'),

    # 这个index函数还没有呢，就在那个文件夹里面编写
    #转过头来居然忘记是在这里编辑了，那边编写好就什么都忘了。
    #其实真的，我懒于做的事情，可能也就只花那么几分钟，甚至不到，没什么好畏惧的。
    #path('admin/', admin.site.urls),


    path('_and/',views._and,name='_and'),
    path('_or/',views._or,name='_or'),
    path('_not/',views._not,name='_not'),

    path('ope_add/',views.ope_add,name='ope_add'),
    path('ope_subtract/',views.ope_subtract,name='ope_subtract'),
    path('ope_multiply/', views.ope_multiply, name='ope_multiply'),
    path('ope_divide/', views.ope_divide, name='ope_divide'),
    path('flip/', views.flip, name='flip'),
    path('affine_trans/', views.affine_trans, name='affine_trans'),

    path('erosion/', views.erosion, name='erosion'),
    path('dilation/', views.dilation, name='dilation'),
    path('morph_open/', views.morph_open, name='morph_open'),
    path('morph_close/', views.morph_close, name='morph_close'),
    path('neighbor_aver/', views.neighbor_aver, name='neighbor_aver'),
    path('median_filter/', views.median_filter, name='median_filter'),
    path('ele_roberts/', views.ele_roberts, name='ele_roberts'),
    path('sobel/', views.sobel, name='sobel'),
    path('prewitt/', views.prewitt, name='prewitt'),
    path('laplacian/', views.laplacian, name='laplacian'),
    path('lowpass_filter/', views.lowpass_filter, name='lowpass_filter'),




    path('butterworth_low_filter/', views.butterworth_low_filter, name='butterworth_low_filter'),
    path('highpass_filter/', views.highpass_filter, name='highpass_filter'),


    path('butterworth_high_filter/', views.butterworth_high_filter, name='butterworth_high_filter'),
    path('robs/', views.robs, name='robs'),
    path('sob/', views.sob, name='sob'),
    path('lap/', views.lap, name='lap'),
    path('log/', views.log, name='log'),
    path('cny/', views.cny, name='cny'),


    path('noise_desc/', views.noise_desc, name='noise_desc'),
    path('aver_filter/', views.aver_filter, name='aver_filter'),
    path('sort_filter/', views.sort_filter, name='sort_filter'),
    path('opt_filter/', views.opt_filter, name='opt_filter'),
    path('line_change/', views.line_change, name='line_change'),






]
