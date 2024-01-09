from .serializers import QuizSerializer, QuestionSerializer, ArticleSerializer, QuizProgressSerializer, QuizWelcomePageSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Quiz, Question, Article, Answer
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
import django_filters
from rest_framework.pagination import PageNumberPagination


class ArticleFilter(django_filters.FilterSet):
    category = filters.AllValuesMultipleFilter(field_name='category__id')

    class Meta:
        model = Article
        fields = ['category']


class ArticlePagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class ArticleListByCategory(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Article.objects.filter(category=category)


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return super().get_queryset()


class ArticleDetailedView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class QuizFilter(django_filters.FilterSet):
    category = filters.AllValuesMultipleFilter(field_name='category__id')

    class Meta:
        model = Quiz
        fields = ['category']


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuizFilter

    def get_queryset(self):
        return super().get_queryset()


class QuizListByCategory(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Quiz.objects.filter(category=category)


class QuizWelcomePageView(generics.ListAPIView):
    def get(self, request, quiz_id=None, format=None):
        if quiz_id is not None:
            try:
                quiz = Quiz.objects.get(pk=quiz_id)
            except Quiz.DoesNotExist:
                return Response({"error": "Quiz not found"}, status=404)

            serializer = QuizWelcomePageSerializer(quiz)
        else:
            quizzes = Quiz.objects.all()
            serializer = QuizWelcomePageSerializer(quizzes, many=True)

        return Response(serializer.data)


class QuizQuestion(APIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self, request, quiz_id, format=None, **kwargs):
        try:
            questions = Question.objects.filter(quiz__id=quiz_id)
        except Question.DoesNotExist:
            return Response({"error": "Questions not found for the specified quiz"}, status=status.HTTP_404_NOT_FOUND)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class QuizProgressView(APIView):
    def get(self, request, quiz_id):
        try:
            quiz = Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            return Response({"error": "Quiz not found"}, status=404)

        total_questions = quiz.get_question_count()
        correct_answers = Answer.objects.filter(
            question__quiz=quiz, is_right=True).count()

        serializer = QuizProgressSerializer({
            "total_questions": total_questions,
            "correct_answers": correct_answers,
        })

        return Response(serializer.data)
