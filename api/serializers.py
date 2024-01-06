from rest_framework import serializers
from .models import Quiz, Question, Answer, Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    total_questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ["id", "title", "quiz_cover", "total_questions", "category"]

    def get_total_questions(self, obj):
        return obj.get_question_count()


class QuizWelcomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["id", "title", "quiz_cover", "welcome_page"]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ["id", "answer_text", "is_right",]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ["quiz", "title", "answer",]


class QuizProgressSerializer(serializers.Serializer):
    total_questions = serializers.IntegerField()
    correct_answers = serializers.IntegerField()
