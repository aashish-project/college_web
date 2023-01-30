from django.contrib import admin
from django.urls import path,include
from dot_learn_app.views import *
urlpatterns = [
    path('',display_data,name='home'),
    path('branch/<str:branch_slug>/',display_data,name="branch"),
    path('branch/<str:branch_slug>/subject/<str:subject_slug>/',display_data,name="branch+sub"),
    path('branch/<str:branch_slug>/subject/<str:subject_slug>/chapter/<str:chapter_slug>',display_data,name="branch+sub+chap"),
    path("topic/<str:topic_slug>/",display_data,name="branch+sub+chap+topic"),
    path('practice',temp,name='practice'),
    path('material',temp,name='material'),
    path('contact',temp,name='contact'),
    path('topic/',question_list,name='topic'),
]
