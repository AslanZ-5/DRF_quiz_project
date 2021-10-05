from django.db import models
from django.utils.translation import gettext_lazy


class Quizzes(models.Model):
    class Meta:
        verbose_name = ('Quiz')
        verbose_name_plural = gettext_lazy('Quizzes')
        ordering = ['id']

    title = models.CharField(max_length=255, default=gettext_lazy('New Quiz'), verbose_name=gettext_lazy('Quiz Title'))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    type = (
        (0, gettext_lazy('ответ с текстом')),
        (1, gettext_lazy('ответ с выбором одного варианта')),
         (2, gettext_lazy('ответ с выбором нескольких вариантов')),
    )
    technique = models.IntegerField(choices=type, default=0, verbose_name=gettext_lazy('Type of Question'))
    title = models.CharField(max_length=255, verbose_name=gettext_lazy('Title'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=gettext_lazy('Date Created'))

    class Meta:
        verbose_name = gettext_lazy('Question')
        verbose_name_plural = gettext_lazy('Questions')
        ordering = ['id']

    def __str__(self):
        return self.title


class Answer(models.Model):
    Question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=255, verbose_name=gettext_lazy('Answer Text'))
    class Meta:
        verbose_name = gettext_lazy('Answer')
        verbose_name_plural = gettext_lazy('Answers')
        ordering = ['id']

    def __str__(self):
        return self.text


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=('Last Updated'), auto_now=True)

    class Meta:
        abstract = True
