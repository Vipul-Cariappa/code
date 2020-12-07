from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
from .functions import check_answer, evaluate_answer

# Create your views here.


def index(request):
    return render(request, 'challenge/index.html', {})


@login_required
def question_new(request):
    active_user = request.user

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post = form.save(commit=False)
            ans = form.cleaned_data.get('solution')
            test = form.cleaned_data.get('test_case')
            if check_answer(ans):
                try:
                    score = evaluate_answer(ans, test)
                except AssertionError:
                    return redirect('challenge:fail')
            active_user = request.user
            post.created_by = active_user
            post.save()
            messages.success(request, f"Question Created")
            return redirect('challenge:home')
    else:
        form = QuestionForm()

    context = {
        'form': form,
    }

    return render(request, 'challenge/new_challenge.html', context)


@login_required
def answer(request, question_id):
    active_user = request.user
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            ans = form.cleaned_data.get('answer')
            if check_answer(ans):
                try:
                    score = evaluate_answer(ans, question.test_case)
                except AssertionError:
                    return redirect('challenge:fail')

            post.question = question
            post.memory = score[0]
            post.time = score[1]
            post.character = score[2]
            active_user = request.user
            post.user = active_user
            post.save()
            messages.success(request, f"Answerd")
            return redirect('challenge:home')
    else:
        form = AnswerForm()

    context = {
        'form': form,
        'question': question
    }

    return render(request, 'challenge/answer.html', context)


def fail(request):
    return render(request, 'challenge/fail.html', {})
