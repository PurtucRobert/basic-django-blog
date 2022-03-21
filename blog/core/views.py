from django.shortcuts import render

# Create your views here.


def front_page(request):
    return render(request, 'core/frontpage.html')


def about_page(request):
    return render(request, 'core/aboutpage.html')
