from django.urls import path
from .views import QuizListView, RandomQuestion, QuizQuestion, ArticleListView, ArticleDetailedView


app_name = 'api'

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz'),
    path('articles/', ArticleListView.as_view(), name='article'),
    path('articles/<int:pk>/', ArticleDetailedView.as_view(), name='article-detail'),
    path('quizzes/r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('quizzes/q/<str:topic>/', QuizQuestion.as_view(), name='question'),
]
