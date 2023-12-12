from django.urls import path

from .views import home, QuizListView, QuestionListView, QuizDetailView, QuizCreateView, QuestionCreateView

urlpatterns = [
    path("", home, name="home"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
    path("quiz/<int:pk>", QuizDetailView.as_view(), name="quiz_detail"),
    path("quiz/create", QuizCreateView.as_view(), name="quiz_create"),
    path("quiz/<int:quiz_id>/questions/", QuestionListView.as_view(), name="question_list"),
    path("quiz/<int:quiz_id>/questions/create", QuestionCreateView.as_view(), name="question_create")
]