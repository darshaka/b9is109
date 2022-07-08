from django.db import models
from django.contrib.auth.models import User


class NewspaperTitle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NewsArtical(models.Model):
    newsAdmin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    newspaperTitle = models.ForeignKey(NewspaperTitle, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    descriptoin = models.TextField(null=True, blank=True)
    subscribers = models.ManyToManyField(
        User, related_name='subscribers', blank=True
    )
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updatedAt']

    def __str__(self):
        return self.name

class NewsComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    newspaper = models.ForeignKey(NewsArtical, on_delete=models.CASCADE)
    commentInfo = models.TextField()
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updatedAt']

    def __str__(self):
        return self.commentInfo[0:100]
