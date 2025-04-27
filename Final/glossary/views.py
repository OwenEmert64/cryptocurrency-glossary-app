from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import JsonResponse
from .models import Term

# Home Page
def index(request):
    return render(request, 'glossary/index.html')

# Signup Page
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'glossary/signup.html', {'form': form})

# Glossary Main Page - Search + Filter
@login_required
def glossary(request):
    terms = Term.objects.all()
    categories = Term.objects.values_list('category', flat=True).distinct()

    category = request.GET.get('category')
    if category and category != 'All':
        terms = terms.filter(category=category)

    query = request.GET.get('q')
    if query:
        terms = terms.filter(models.Q(term__icontains=query) | models.Q(definition__icontains=query))

    return render(request, 'glossary/glossary.html', {
        'terms': terms,
        'categories': categories,
    })

# Create Term
@login_required
def create_term(request):
    if request.method == 'POST':
        term = request.POST.get('term')
        definition = request.POST.get('definition')
        category = request.POST.get('category')
        if term and definition:
            Term.objects.create(
                term=term,
                definition=definition,
                category=category,
                added_by=request.user
            )
            return redirect('glossary')
    return render(request, 'glossary/create_term.html')

# Edit Term
@login_required
def edit_term(request, term_id):
    term = get_object_or_404(Term, id=term_id, added_by=request.user)
    if request.method == 'POST':
        term.term = request.POST.get('term')
        term.definition = request.POST.get('definition')
        term.category = request.POST.get('category')
        term.save()
        return redirect('glossary')
    return render(request, 'glossary/edit_term.html', {'term': term})

# Delete Term
@login_required
def delete_term(request, term_id):
    term = get_object_or_404(Term, id=term_id, added_by=request.user)
    if request.method == 'POST':
        term.delete()
        return redirect('glossary')
    return render(request, 'glossary/delete_term.html', {'term': term})

# Favorite/Unfavorite Term
@login_required
def toggle_favorite(request, term_id):
    term = get_object_or_404(Term, id=term_id)

    if request.user in term.favorited_by.all():
        term.favorited_by.remove(request.user)
    else:
        term.favorited_by.add(request.user)

    return redirect('glossary')

# Profile Page - Show Favorited Terms
@login_required
def profile(request):
    favorites = request.user.favorites.all()
    return render(request, 'glossary/profile.html', {
        'favorites': favorites
    })

# Search Terms (AJAX/JavaScript Search)
@login_required
def search_terms(request):
    query = request.GET.get('q', '')
    results = Term.objects.filter(term__icontains=query).values('term', 'definition', 'category')
    return JsonResponse(list(results), safe=False)
