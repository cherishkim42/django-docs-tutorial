import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# Each model is repped by a class that subclasses django.db.models.Model.
# Each model has CLASS VARIABLES, each of which reps a DB FIELD in the model.
# Each field is repped by an instance of a Field class (ex. CharField for character fields; DateTimeField for datetimes)

#models.Model = go to models library, use the Model class from there
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text