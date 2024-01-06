from .serializers import QuizSerializer, QuestionSerializer, ArticleSerializer, QuizProgressSerializer, QuizWelcomePageSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Quiz, Question, Article, Answer
from rest_framework.views import APIView
from rest_framework import status


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        if category_id:
            return Quiz.objects.filter(category_id=category_id)
        else:
            return Quiz.objects.all()


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        if category_id:
            return Article.objects.filter(category_id=category_id, is_active=True)
        else:
            return Article.objects.all()


class ArticleDetailedView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class QuizWelcomePageView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizWelcomePageSerializer


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
