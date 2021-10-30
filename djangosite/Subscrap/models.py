from django.db import models

# Create your models here.


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


class SubscriptionList(models.Model):
    # name of person
    name = models.CharField(max_length=200)
    # name of List
    listName = models.CharField(max_length=200)
    # id of person
    id = models.IntegerField(max_length=100)

    def __str__(self):
        return self.listName


class SubscriptionItem(models.Model):
    SubscriptionList = models.ForeignKey(
        SubscriptionList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    id = models.IntegerField(max_length=100)
    startDate = models.DateTimeField()
    expirationDate = models.DateTimeField()
    postitionInList = models.IntegerField()
    muted = models.BooleanField()

    def __str__(self):
        return self.name
