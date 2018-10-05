from django.http import HttpResponse
# Create your views here.


def first_hack(request):
    return HttpResponse("<h1>This is first hacking program.</h1>")