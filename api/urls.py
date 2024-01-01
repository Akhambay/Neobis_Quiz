from django.urls import path
from .views import Quiz, RandomQuestion


app_name = 'api'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
]
