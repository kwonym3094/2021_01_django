from django import forms
from .models import Question, Answer, Comment


# django form class
#   1. forms.Form: 폼
#   2. forms.ModelForm : 모델폼 => 모델과 연결된 폼, 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있음
#                        장고 모델폼은 내부 클래스로 Meta 클래스를 반드시 가져야함, Meta 클래스에서는 모델 폼이 사용할 모델과 모델의 필드들을 적어야 함


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]
        # widgets = {
        #     "subject": forms.TextInput(attrs={"class": "form-control"}),
        #     "content": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
        # }
        labels = {"subject": "제목", "content": "내용"}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
        labels = {
            "content": "답변내용",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {
            "content": "댓글내용",
        }