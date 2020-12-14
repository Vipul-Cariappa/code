from django.shortcuts import render

# Create your views here.


def functions(request):
    return render(request, 'tutorial/functions.html', {})
