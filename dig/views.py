from django.http import HttpResponse

def serverHomepage(request):
    return HttpResponse('<h1>Server homepage from template here & other js & css files</h1>')
