from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  # Link author to another model called auth
  author = models.ForeignKey('auth.User')
  # Define title as a text field with characters maxed at 200
  title = models.CharField(max_length=200)
  # Define text as a text field with no limit
  text = models.TextField()
  # Define created and published date as Date and Time field
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title
