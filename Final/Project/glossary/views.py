from django.shortcuts import render
from .models import Term

def index(request):
    terms = Term.objects.all().order_by('title')
    return render(request, 'glossary/index.html', {'terms': terms})
