from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,template_name='main/index.html')


def blog(request):
    return render(request,template_name='main/blog.html')


def post(request):
    return render(request,template_name='main/post.html')


def about(request):
    return render(request,template_name='main/about.html')


def join_us(request):
    return render(request,template_name='main/join.html')


def events(request):
    return render(request,template_name='main/events.html')


def resources(request):
    return render(request,template_name='main/resources.html')


def services(request):
    return render(request,template_name='main/services.html')


def contact(request):
    return render(request,template_name='main/contact.html')
