# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages

from . models import *

# Create your views here.


def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)


def add(request):
    if request.method == 'POST':
        errors = Course.objects.course_validator(request.POST)

        if len(errors):
            for error in errors:
                messages.error(request, error)
        else:
            Course.objects.add_course(request.POST)

        return redirect('/')
    else:
        return redirect('/')


def remove(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'course_app/confirm.html', context)


def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()

    return redirect('/')


def comment(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
        'comments': Comment.objects.filter(course_id__id=course_id)
    }
    return render(request, 'course_app/comments.html', context)


def add_comment(request, course_id):
    if request.method == 'POST':
        comment = Comment.objects.add_comment(request.POST, course_id)

        return redirect('/' + course_id + '/comment')
    else:
        return redirect('/' + course_id + '/comment')


def delete_comment(request, course_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return redirect('/' + course_id + '/comment')
