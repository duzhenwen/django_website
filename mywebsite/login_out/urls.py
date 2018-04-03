from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
   # url(r'^login/$',auth_views.login,name="user_login"),
    url(r'^logout/$',auth_views.logout,name="user_logout"),
    url(r'^register/$',views.Register,name="register"),
    url(r'^login/',views.Login,name="user_login"),
    url(r'^content/',views.content),
]
