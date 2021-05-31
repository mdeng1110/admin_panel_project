from django.urls import include, path
from api import views


urlpatterns = [
    path(r'instructors/add', views.instructor_add),
    path(r'instructors/list', views.instructor_list),
    path(r'instructors/<int:pk>/describe', views.instructor_describe),
    path(r'instructors/<int:pk>/update', views.instructor_update),
    path(r'instructors/<int:pk>/remove', views.instructor_remove),
    path(r'courses/add', views.course_add),
    path(r'courses/list', views.course_list),
    path(r'courses/<int:pk>/describe', views.course_describe),
    path(r'courses/<int:pk>/update', views.course_update),
    path(r'courses/<int:pk>/remove', views.course_remove)
]