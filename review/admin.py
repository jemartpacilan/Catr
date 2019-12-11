from django.contrib import admin
from .models import Review, Question, Answer

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['caterer']}),
        (None, {'fields': ['consumer']}),
        (None, {'fields': ['review_body']}),
        (None, {'fields': ['review_rating']}),
    ]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['caterer']}),
        (None, {'fields': ['consumer']}),
        (None, {'fields': ['question_body']}),
    ]


class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        (None, {'fields': ['caterer']}),
        (None, {'fields': ['answer_body']}),
    ]


admin.site.register(Review, ReviewAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
