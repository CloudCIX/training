# libs
from cloudcix_rest.models import BaseModel, BaseManager
from django.db import models
from django.urls import reverse
# local
from .cls import Cls


__all__ = [
    'Student',
]


class StudentManager(BaseManager):
    def get_queryset(self) -> models.QuerySet:
        """
        Extend the BaseManager QuerySet to prefetch all related data in every query to speed up serialization
        :return: A base queryset which can be further extended but always prefetches necessary data
        """
        return super().get_queryset().select_related(
            'cls',
            'cls__syllabus',
        )


class Student(BaseModel):
    """A Student record describes a Student"""
    cls = models.ForeignKey(Cls, models.CASCADE)
    notes = models.TextField(null=True)
    user_id = models.IntegerField()

    objects = StudentManager()

    class Meta:
        db_table = 'student'
        indexes = [
            models.Index(fields=['id'], name='student_id'),
            models.Index(fields=['notes'], name='student_notes'),
            models.Index(fields=['user_id'], name='student_user_id'),
        ]

    def get_absolute_url(self):
        """
        Generates the absolute URL that corresponds to the StudentResource view for this Student record
        :return: A URL that corresponds to the views for this Student record
        """
        return reverse('student_resource', kwargs={'pk': self.pk})
