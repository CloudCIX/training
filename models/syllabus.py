# libs
from cloudcix_rest.models import BaseModel
from datetime import datetime
from django.db import models
from django.urls import reverse


__all__ = [
    'Syllabus',
]


class Syllabus(BaseModel):
    """
    A Syllabus record describes a Syllabus
    """
    description = models.TextField()
    member_id = models.IntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'syllabus'
        indexes = [
            models.Index(fields=['id'], name='syllabus_id'),
            models.Index(fields=['deleted'], name='syllabus_deleted'),
            models.Index(fields=['name'], name='syllabus_name'),
        ]

    def get_absolute_url(self):
        """
        Generates the absolute URL that corresponds to the SyllabusResource view for this Syllabus record
        :return: A URL that corresponds to the views for this Syllabus record
        """
        return reverse('syllabus_resource', kwargs={'pk': self.pk})

    def cascade_delete(self):
        """
        Set the deleted timestamp of this Object to the current time,
        and call this method on all of the Child Objects belonging to this Object
        """
        self.deleted = datetime.utcnow()
        self.save()

        # Also delete Child Objects
        for obj in self.classes.iterator():
            obj.deleted = datetime.utcnow()
            obj.save()
