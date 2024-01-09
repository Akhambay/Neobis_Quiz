from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Quiz(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    quiz_cover = models.ImageField(
        null=True, blank=True, default='/quiz_pics/default.png', upload_to='quiz_pics')
    welcome_page = models.TextField(max_length=500, default=_(
        "Добро пожаловать на квиз"))

    def get_question_count(self):
        return self.question.count()

    def get_user_quiz_progress(self, user_answers):
        total_questions = self.get_question_count()
        correct_answers = sum(user_answers.values_list('is_right', flat=True))
        return correct_answers, total_questions

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name=_("Last updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    quiz = models.ForeignKey(
        Quiz, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name="Title")
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active status"))

    def __str__(self):
        return self.title


class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Article(models.Model):

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ['id']

    title = models.CharField(max_length=255, default="New article")
    content = models.TextField(max_length=900, default="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    time_to_read = models.PositiveIntegerField(default=10)  # in minutes
    article_cover = models.ImageField(
        null=True, blank=True, default='/article_pics/default.png', upload_to='article_pics')
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        default=True, verbose_name=_("Active status"))

    def __str__(self):
        return self.title
