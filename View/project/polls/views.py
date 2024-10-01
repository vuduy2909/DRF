# polls/views.py
from django.shortcuts import redirect
from django.urls import reverse

def some_view(request):
    url = reverse('author-polls:index', current_app='author-polls')
    return redirect(url)
