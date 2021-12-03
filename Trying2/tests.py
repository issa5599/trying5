from django.test import TestCase

# Create your tests here.
import datetime
from django.test import Client
from django.utils import timezone
from django.urls import reverse

from .models import lesson


class lessonModelTests(TestCase):

    def was_published_recently_with_future_cour(self):
        """
        was_published_recently() returns False for lesson whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_lesson = lesson(pub_date=time)
        future_question=lesson(startedfrom=time)
        self.assertIs(future_question.was_published_recently(), False)
        self.assertIs(future_lesson.was_published_recently(), False)


#Here we have created a django.test.TestCase subclass with a method that creates a Question instance with a pub_date in the future. We then check the output of was_published_recently() - which ought to be False.
def was_published_recently_with_recent_lesson(self):
    """
    was_published_recently() returns True for lesson whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_lesson = lesson(pub_date=time)
    self.assertIs(recent_lesson.was_published_recently(), True)
    