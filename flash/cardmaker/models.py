from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Student(models.Model):

    full_name =  models.CharField(max_length=200)


    def __str__(self):
        return self.full_name


class Stack(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('create_cards', kwargs={'stack_id':self.id})


class Card(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
