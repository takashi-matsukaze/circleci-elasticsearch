from django.shortcuts import render
from haystack.query import SearchQuerySet

from .models import Note


def index(request):
    notes = SearchQuerySet().models(Note).filter(title='Hoge')
    context = {'notes': notes}
    return render(request, 'blog/index.html', context)
