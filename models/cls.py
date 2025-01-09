# libs
from cloudcix_rest.models import BaseModel, BaseManager
from django.db import models
from django.urls import reverse
# local
from .syllabus import Syllabus


__all__ = [
    'Cls',
]


class ClsManager(BaseManager):
    def get_queryset(self) -> models.QuerySet:
        """
        Extend the BaseManager QuerySet to prefetch all related data in every query to speed up serialization
        :return: A base queryset which can be further extended but always prefetches necessary data
        """
        return super().get_queryset().select_related(
            'syllabus',
        )


class Cls(BaseModel):
    """
    A Class record describes a Class
    """
    finish_date = models.DateTimeField(null=True)
    start_date = models.DateTimeField()
    syllabus = models.ForeignKey(Syllabus, models.CASCADE, related_name='classes')
    trainer = models.CharField(max_length=50)

    objects = ClsManager()

    class Meta:
        db_table = 'cls'
        indexes = [
            models.Index(fields=['id'], name='cls_id'),
            models.Index(fields=['deleted'], name='cls_deleted'),
            models.Index(fields=['finish_date'], name='cls_finish_date'),
            models.Index(fields=['start_date'], name='cls_start_date'),
            models.Index(fields=['trainer'], name='cls_trainer'),
        ]

    def get_absolute_url(self):
        """
        Generates the absolute URL that corresponds to the ClassResource view for this Class record
        :return: A URL that corresponds to the views for this Class record
        """
        return reverse('cls_resource', kwargs={'pk': self.pk})
