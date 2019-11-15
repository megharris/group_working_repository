from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'sis'
urlpatterns = [
    path('', views.student_home, name='student_home'),
    #re_path(r'^home/$', views.home, name='home'),
    path('tutor_list', views.tutor_list, name='tutor_list'),
    path('course_list', views.course_list, name='course_list'),
    path('schedule_list', views.schedule_list, name='schedule_list'),
    path('register/', views.register, name='register'),
]