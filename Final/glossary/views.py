from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'glossary/index.html')

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


from .models import Term
from django.contrib.auth.decorators import login_required

@login_required
def glossary_view(request):
    terms = Term.objects.all().order_by('term')
    return render(request, 'glossary/glossary.html', {'terms': terms})