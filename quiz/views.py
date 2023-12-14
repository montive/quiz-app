from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import CreateQuiz, CreateQuestion
from .models import Quiz, Question, Answer


def home(request):
    return render(request, "home.html")


class QuizListView(ListView):
    model = Quiz
    template_name = "quiz_list.html"


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz_detail.html"


class QuizCreateView(CreateView):
    model = Quiz
    template_name = "quiz_create.html"
    form_class = CreateQuiz
    success_url = reverse_lazy("quiz_list")


class QuestionListView(ListView):
    model = Question
    template_name = "question_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quiz_id"] = self.kwargs["quiz_id"]
        return context


class QuestionCreateView(CreateView):
    model = Question
    template_name = "question_create.html"
    form_class = CreateQuestion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quiz_id"] = self.kwargs["quiz_id"]
        return context

    def form_valid(self, form):
        form.instance.quiz_id = self.kwargs["quiz_id"]
        return super(QuestionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("question_list", kwargs={"quiz_id": self.object.quiz_id})
