import json

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from pyutility import limit_resource, measureit

from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
from .functions import validate, run_tests

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

            if validate(ans):

                try:
                    limit_resource(run_tests, time=15,
                                   memory=75, args=(ans, test))
                except AssertionError:
                    messages.success(request, f"Assertion Error")
                    return redirect('challenge:fail')
                except TimeoutError:
                    messages.success(request, f"Time Out Error")
                    return redirect('challenge:fail')
                except MemoryError:
                    messages.success(request, f"Memory Error")
                    return redirect('challenge:fail')
                except Exception as e:
                    messages.success(request, f"{e}")
                    return redirect('challenge:fail')
            else:
                messages.success(
                    request, f"Bad Function Name or Other problem")
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


def answer_test(request, question_id):
    active_user = request.user
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":

        ans = json.loads(request.body.decode("utf-8")
                         )["solution"]  # this can raise error

        if validate(ans):

            try:
                limit_resource(run_tests, time=15,
                               memory=75, args=(ans, question.test_case))
            except AssertionError:
                content = {"result": "failed", "error": "Assertion Error"}
            except TimeoutError:
                content = {"result": "failed", "error": "Timeout Error"}
            except MemoryError:
                content = {"result": "failed", "error": "Memory Error"}
            except Exception as e:
                content = {"result": "failed", "error": f"{e}"}
            else:
                content = {"result": "passed"}
        else:
            content = {"result": "failed",
                       "error": "Bad Function Name or Other problem"}
    else:
        content = {}

    return HttpResponse(json.dumps(content), content_type="application/json")


@login_required
def answer(request, question_id):
    active_user = request.user
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            ans = form.cleaned_data.get('answer')
            score = measureit(run_tests, args=(
                ans, question.test_case))

            post.question = question
            post.memory = score[0]
            post.time = score[1]
            post.character = len(ans)
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


def question_list(request):
    li = Question.objects.all()
    return render(request, "challenge/question_list.html", {"questions": li})


def result_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, "challenge/answer_list.html", {"answers": answers})


def answer_view(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    return render(request, "challenge/answer_view.html", {"answer": answer})
