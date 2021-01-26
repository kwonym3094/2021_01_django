from django.core.paginator import Paginator
from ..models import Question
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """

    # 입력파라미터
    page = request.GET.get("page", "1")  # 페이지
    kw = request.GET.get("kw", "")
    so = request.GET.get("so", "recent")
    # GET 요청방식의 예: localhost:8000/pybo/?page=1

    # 정렬
    if so == "recommend":
        question_list = Question.objects.annotate(num_vote=Count("vote")).order_by(
            "-num_vote", "-create_date"
        )
    elif so == "popular":
        question_list = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-create_date"
        )
    else:
        question_list = Question.objects.order_by("-create_date")

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)
            | Q(content__icontains=kw)
            | Q(author__username__icontains=kw)
            | Q(answer__author__username__icontains=kw)
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj, "page": page, "kw": kw, "so": so}
    return render(request, "pybo/question_list.html", context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)