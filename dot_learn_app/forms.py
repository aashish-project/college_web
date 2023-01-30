from django.contrib.admin.options import StackedInline
from .models import Chapter, Topic, Question, Answer, Category

class ChapterInlineForm(StackedInline):
    model = Chapter
    fields = ['chapter']

class TopicInlineForm(StackedInline):
    model = Topic
    fields = ['topic1',"topic2","topic3"]

# class QuestionInlineForm(StackedInline):
#     model = Question
#     fields = ['question']

class AnswerInlineForm(StackedInline):
    model = Answer
    fields = ['answer']

class CategoryInlineForm(StackedInline):
    model = Category
    fields = ['category']
