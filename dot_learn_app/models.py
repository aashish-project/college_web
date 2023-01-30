from django.db import models
import uuid
import django.utils.timezone
from datetime import datetime
# Create your models here. 

class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch=models.CharField( max_length=100)

    def __str__(self):
        return self.branch
    
class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch=models.ForeignKey( Branch, on_delete=models.CASCADE, default=None)
    subject=models.CharField(max_length=100)

    def __str__(self):
        return self.subject
    
class Chapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject=models.ForeignKey( Subject, on_delete=models.CASCADE, default=None)
    chapter=models.CharField(max_length=100)

    def __str__(self):
        return self.chapter
    
class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default=None)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, default=None)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    
class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created=models.DateTimeField(default=datetime.now, null=True, blank=True)
    updated = models.DateTimeField(default=datetime.now, null=True, blank=True)
    topic=models.ForeignKey( Topic, on_delete=models.CASCADE, default=None)
    question=models.CharField( max_length=100)

    def __str__(self):
        return self.question
    
class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question=models.ForeignKey( Question, on_delete=models.CASCADE, default=None)
    answer=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.answer
    
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch_related=models.ForeignKey(Branch, on_delete=models.CASCADE, default=None)
    question=models.ForeignKey( Question, on_delete=models.CASCADE, default=None)
    year=models.IntegerField(default=0000)
    related=models.CharField( max_length=100)
