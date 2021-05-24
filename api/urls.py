from django.urls import include, path
from .views import InstructorCreate, InstructorList, InstructorDetail, InstructorUpdate, InstructorDelete


urlpatterns = [
    path('create/', InstructorCreate.as_view(), name='create-Instructor'),
    path('', InstructorList.as_view()),
    path('<int:pk>/', InstructorDetail.as_view(), name='retrieve-Instructor'),
    path('update/<int:pk>/', InstructorUpdate.as_view(), name='update-Instructor'),
    # path('delete/<int:pk>/', InstructorDelete.as_view(), name='delete-Instructor')
]