# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect

from . models import *
from ..users.models import *

from django.contrib import messages

# Create your views here.


def index(request):
    if 'user' in request.session:
        current_user = User.objects.get(id=request.session['user'])

        context = {
            'user': current_user,
            'books': Book.objects.order_by('created_at').reverse()[:5],
            'reviews': Review.objects.all(),
            'all_books': Book.objects.all()
        }
        return render(request, 'book_reviews/books.html', context)

    else:
        return HttpResponseRedirect(reverse('login:index'))
