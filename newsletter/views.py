from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'newsletter/home.html', {'articles': articles})
