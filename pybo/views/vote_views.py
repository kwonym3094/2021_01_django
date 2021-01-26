from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer


@login_required(login_url="common:login")
def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        question.vote.add(request.user)
    return redirect("pybo:details", question_id=question_id)


@login_required(login_url="common:login")
def vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        answer.vote.add(request.user)
    return redirect("pybo:details", question_id=answer.question.id)
