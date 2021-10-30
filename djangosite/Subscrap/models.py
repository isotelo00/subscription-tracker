from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# Test code


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

    # Real Code


class SubscriptionList(models.Model):
    # name of List
    listName = models.CharField(max_length=200)
    # id of user
    Tempid = models.IntegerField()
    # User
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.listName


class SubscriptionItem(models.Model):
    SubscriptionList = models.ForeignKey(
        SubscriptionList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    Tempid = models.IntegerField()
    startDate = models.DateTimeField(auto_now_add=True)
    expirationDate = models.DateTimeField(default=timezone.now)
    postitionInList = models.IntegerField()
    muted = models.BooleanField()

    def __str__(self):
        return self.name
