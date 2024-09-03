"""
URL configuration for School project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('Techlog/',views.Techlog,name="Techlog"),
    path('TLogout/',views.tlogout,name='tlogout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboardGet/',views.dashboardGet,name='dashboardGet'),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    re_path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
    path('dashviewteach/',views.dashviewteach,name="dashviewteach"),
    path('mark/',views.mark,name="mark"),
    path('graph/',views.graph,name='graph'),
    path('sregister/',views.sregister,name='sregister'),
    path('slogin/',views.slogin,name='slogin'),
    path('studash/',views.studash,name='studash'),
    path('slogout/',views.slogout,name='slogout'),
    path('stable/',views.stable,name='stable'),
    path('mtable/',views.mtable,name='mtable'),
    path('supdate/<int:id>',views.supdate,name="supdate"),
    re_path(r'^delete_mark/(?P<pk>[0-9]+)/$',views.sdelete,name="sdelete"),
    # path('smarkget/',views.smarkget,name='smarkget'),
    path('sedit/<int:id>',views.sedit,name="sedit"),
]
