from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

# Create your views here.
def index(request):
    question_list = Question.objects.order_by("-create_date")
    context = {"question_list": question_list}
    return render(request, "practice/question_list.html", context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "practice/question_details.html", context=context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("practice:details", question_id=question.id)
    else:
        form = AnswerForm()
    context = {
        "question": question,
        "form": form,
    }

    return render(request, "practice/question_details.html", context)


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect("practice:index")
    else:
        form = QuestionForm()
    context = {"form": form}
    return render(request, "practice/question_form.html", context)
