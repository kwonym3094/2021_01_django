from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """

    # 입력파라미터
    page = request.GET.get("page", "1")  # 페이지
    # GET 요청방식의 예: localhost:8000/pybo/?page=1

    # 조회
    question_list = Question.objects.order_by("-create_date")

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj}
    return render(request, "pybo/question_list.html", context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)


# genric view: 목록 조회나 상세조회처럼 특정 패턴이 있는 뷰를 작성할 때 사용하는 편리한 기능 => 실행방식이 이해하기 어려움

# class IndexView(generic.ListView):
#     def get_queryset(self):
#         # 템플릿명을 명시적으로 지정하지 않으면 자동으로 '모델명_list.html'을 사용함
#         return Question.objects.order_by("-create_date")


# class DetailView(generic.DetailView):
#     model = Question


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("pybo:details", question_id=question.id)
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "pybo/question_detail.html", context)


def question_create(request):

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")
    else:
        form = QuestionForm()
    context = {"form": form}
    return render(request, "pybo/question_form.html", context)
