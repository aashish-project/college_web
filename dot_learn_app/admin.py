from django.contrib import admin
# from django.contrib.admin.options import StackedInline
from .models import *
# Register your models here.
class ChapterInlineForm(admin.StackedInline):
    model = Chapter

class TopicInlineForm(admin.StackedInline):
    model = Topic

class AnswerInlineForm(admin.StackedInline):
    model = Answer

class CategoryInlineForm(admin.StackedInline):
    model = Category

class SubjectAdmin(admin.ModelAdmin):
    inlines = [ChapterInlineForm ]
class ChapterAdmin(admin.ModelAdmin):
    inlines = [TopicInlineForm]
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineForm , CategoryInlineForm]
class TopicAdmin(admin.ModelAdmin):
    list_display = ('branch', 'subject', 'chapter', 'topic')
    list_filter = ('branch', 'subject', 'chapter')
admin.site.register(Branch)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Category)