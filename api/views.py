from .serializers import QuizSerializer, QuestionSerializer, ArticleSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Quiz, Question, Article
from rest_framework.views import APIView


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetailedView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class QuizQuestion(APIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self, request, format=None, **kwargs):
        quiz_title = kwargs['topic']
        question = Question.objects.filter(
            quiz__title=quiz_title)
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
