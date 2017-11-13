from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add),
    url(r'^(?P<course_id>\d+)/remove$', views.remove),
    url(r'^(?P<course_id>\d+)/delete$', views.delete),
    url(r'^(?P<course_id>\d+)/comment$', views.comment),
    url(r'^(?P<course_id>\d+)/add_comment$', views.add_comment),
    url(r'^(?P<course_id>\d+)/(?P<comment_id>\d+)/delete$', views.delete_comment),

]
