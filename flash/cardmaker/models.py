from django.db import models

# Create your models here.
class Student(models.Model):
    full_name =  models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class Stack(models.Model):
    subject = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Card(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Stack, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
