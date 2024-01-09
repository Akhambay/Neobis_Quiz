from django.urls import path
from .views import QuizListView, QuizQuestion, ArticleListView, ArticleDetailedView, QuizProgressView, QuizWelcomePageView, ArticleListByCategory, QuizListByCategory
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

app_name = 'api'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article'),
    path('articles/<int:pk>/', ArticleDetailedView.as_view(), name='article-detail'),
    path('articles/category/<str:category>/',
         ArticleListByCategory.as_view(), name='article-category'),
    path('quizzes/', QuizListView.as_view(), name='quiz'),
    path('quizzes/<int:quiz_id>/welcome/',
         QuizWelcomePageView.as_view(), name='quiz_welcome_page'),
    path('quizzes/<int:quiz_id>/questions/',
         QuizQuestion.as_view(), name='question'),
    path('quizzes/category/<str:category>/',
         QuizListByCategory.as_view(), name='quiz-category'),
    path('quizzes/<int:quiz_id>/progress/',
         QuizProgressView.as_view(), name='quiz-progress'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
]
