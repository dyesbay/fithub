from api.views import CourseDetail, CourseList, LectureList, LessonList, logout, login, NewsList
from api import views
from django.urls import path

urlpatterns = [
    path('courses/', CourseList.as_view()),
    path('courses/<int:pk>/', CourseDetail.as_view()),
    path('courses/<int:pk>/lectures/', LectureList.as_view()),
    path('courses/<int:pk>/lessons/', LessonList.as_view()),
    path('student/courses/', views.courses_list),
    path('student/courses/<int:pk>/lessons/', views.lessons_list),
    path('student/courses/<int:pk>/lectures/', views.lectures_list),
    path('student/courses/<int:pk>/forums/', views.ForumList.as_view()),
    path('student/courses/<int:pk>/forums/<int:pk1>/', views.TopicList.as_view()),
    path('news/', NewsList.as_view()),
    path('login/', login),
    path('logout/', logout)
]