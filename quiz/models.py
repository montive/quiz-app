from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    grade = models.FloatField(null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answer(models.Model):
    correct_answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.correct_answer
