from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class lesson(models.Model):
    
    all_lesson=models.CharField(max_length=300)
    knowledgeable=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    startedfrom=models.DateTimeField('started from')
    
    def __str__(self):
        return self.all_lesson


class details(models.Model):

    all_lesson=models.ForeignKey(lesson, on_delete=models.CASCADE)
    d1=models.CharField(max_length=300)
    d2=models.BooleanField(default=False)
    numero = models.IntegerField(default=0)
    tb= models.CharField(max_length=300)
    def __str__(self):
        return str(self.tb)

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
    return self.startedfrom >= timezone.now()- datetime.timedelta(days=1 )