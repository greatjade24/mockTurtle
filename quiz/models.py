from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_no = models.IntegerField(primary_key=True, null=False)
    quiz_title = models.CharField(max_length=30, null=False)
    quiz_content = models.CharField(max_length=1000, null=False)
    hint1 = models.CharField(max_length=1000)
    hint2 = models.CharField(max_length=1000)
    hint3 = models.CharField(max_length=1000)
    hint4 = models.CharField(max_length=1000)
    hint5 = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    quiz_summary = models.CharField(max_length=500)
    quiz_image = models.CharField(max_length=200)