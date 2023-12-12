from django import forms

from quiz.models import Quiz, Question, Answer


class CreateQuiz(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["name", "description"]


class CreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title"]


class CreateAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["correct_answer"]
