from django.contrib import admin
from . import models


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title'
    ]


class AnswerAdminInLine(admin.TabularInline):
    model = models.Answer
    fields = [
        'text'
    ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
        'date_created'
    ]

    inlines = [
        AnswerAdminInLine,
    ]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'text',
        'Question',

    ]
