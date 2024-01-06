from django.urls import path
from .views import QuizListView, QuizQuestion, ArticleListView, ArticleDetailedView, QuizProgressView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

app_name = 'api'

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz'),
    path('articles/', ArticleListView.as_view(), name='article'),
    path('articles/<int:pk>/', ArticleDetailedView.as_view(), name='article-detail'),
    path('quizzes/<int:quiz_id>/questions/',
         QuizQuestion.as_view(), name='question'),
    path('quizzes/<int:quiz_id>/progress/',
         QuizProgressView.as_view(), name='quiz-progress'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
]
