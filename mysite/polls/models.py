from django.db import models

# Create your models here.
# Each model is repped by a class that subclasses django.db.models.Model.
# Each model has CLASS VARIABLES, each of which reps a DB FIELD in the model.
# Each field is repped by an instance of a Field class (ex. CharField for character fields; DateTimeField for datetimes)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)