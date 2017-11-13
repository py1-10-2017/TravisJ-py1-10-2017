# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = []

        if len(postData['name']) < 5:
            errors.append('Name must be at least 5 charaters long.')
        if len(postData['desc']) < 15:
            errors.append('Description must be at least 15 characters')

        return errors

    def add_course(self, postData):
        course = Course.objects.create(
            name=postData['name'], description=postData['desc'])
        return course


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()


class CommentManager(models.Manager):
    def add_comment(self, postData, course_id):
        comment = Comment.objects.create(
            comment=postData['comment'], name=postData['title'], course=Course.objects.get(id=course_id))
        return comment


class Comment(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=30)
    course = models.ForeignKey(
        Course, related_name='comments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()
