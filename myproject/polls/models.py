import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class PollUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

class ApiKey(models.Model):
    username = models.CharField(max_length=50)
    api_key = models.CharField(max_length=20)

    def __str__(self):
        return "{} - {}".format(self.username, self.api_key)
