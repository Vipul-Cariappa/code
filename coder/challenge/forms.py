from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("title", "question", "solution", "test_case")

        widgets = {
            'solution': forms.Textarea(attrs={'id': 'solution', }),
            'test_case': forms.Textarea(attrs={'id': 'test_case', }),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("answer",)

        widgets = {
            'answer': forms.Textarea(attrs={'id': 'solution',}),
        }
