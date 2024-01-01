from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Quiz, Question
from rest_framework.views import APIView


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        quiz_title = kwargs['topic']
        question = Question.objects.filter(
            quiz__title=quiz_title).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        quiz_title = kwargs['topic']
        question = Question.objects.filter(
            quiz__title=quiz_title)
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
