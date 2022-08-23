from django.urls import path

from . import views

app_name = 'pybo'   #namespace 이름 설정

urlpatterns = [
    path('', views.index, name='index'),  # pybo/
    path('<int:question_id>/', views.detail, name='detail'),  # pybo/1, pybo/2 등등..
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name="question_create"),
]
