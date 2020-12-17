from django.shortcuts import render

# Create your views here.

TABLE_OF_CONTENT = [
    "intro",
    "input/output",
    "variables",
    "if statements",
    "loops",
    "functions",
]


def intro(request):
    return render(request, 'tutorial/intro.html', {})


def io(request):
    return render(request, 'tutorial/io.html', {})


def variables(request):
    return render(request, 'tutorial/variables.html', {})


def if_statements(request):
    return render(request, 'tutorial/if_statement.html', {})


def loops(request):
    return render(request, 'tutorial/loops.html', {})


def functions(request):
    return render(request, 'tutorial/functions.html', {})
