from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question", "solution", "test_case")


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("answer",)

        widgets = {
            'answer': forms.Textarea(attrs={'id': 'solution'}),
        }
