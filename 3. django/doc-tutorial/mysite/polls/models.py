from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

class Question(models.Model):
    questionText = models.CharField(max_length = 200)
    pubDate = models.DateTimeField('date published')

    def __str__(self):
        # By default, Django displays the str() of each object .
        return self.questionText

    @admin.display(
        boolean = True,
        ordering = 'pubDate',
        description = 'Published recently ?',
    )
    def wasPublishedRecently(self):
        # return self.pubDate >= timezone.now() - datetime.timedelta(days = 1)
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pubDate <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    ChoiceText = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choiceText