from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns= [
    url(r'^forum/$', views.forum , name='forum'),
     url(r'^events/$', views.events , name='events'),
    url(r'^register/$', views.UserFormView.as_view() , name='register'),
    url(r'^login/$', views.login_user , name='login'),
     url(r'^logout/$', views.logout_user , name='logout'),
    url(r'^$', views.index , name='index'),
    url(r'^about/$', views.about , name='about'),
]
