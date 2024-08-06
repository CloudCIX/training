"""
Permissions classes will use their methods to validate permissions for a
request.
These methods will raise any errors that may occur all you have to do is
call the method in the view
"""
# stdlib
from typing import Optional
# libs
from cloudcix_rest.exceptions import Http403
from rest_framework.request import Request
# local
from training.models import Student, Syllabus


class Permissions:

    @staticmethod
    def create(request: Request) -> Optional[Http403]:
        """
        The request to create a new Syllabus record is valid if:
        - The User creating a Syllabus is a self-managed Member
        """
        # The requesting User's Member is self-managed
        if not request.user.member['self_managed']:
            return Http403(error_code='training_syllabus_create_201')
        return None

    @staticmethod
    def read(request: Request, obj: Syllabus) -> Optional[Http403]:
        """
        The request to create a new Syllabus record is valid if:
        - The request is creating a Syllabus in the User's Member
        """
        # The request is creating a Syllabus in the User's Member
        if obj.member_id != request.user.member['id']:
            return Http403(error_code='training_syllabus_read_201')
        return None

    @staticmethod
    def update(request: Request, obj: Syllabus) -> Optional[Http403]:
        """
        The request to update a Syllabus record is valid if:
        - The request is updating a Syllabus in the User's Member
        """
        # The request is updating a Syllabus in the User's Member
        if request.user.member['id'] != obj.member_id:
            return Http403(error_code='training_syllabus_update_201')
        return None

    @staticmethod
    def delete(request: Request, obj: Syllabus) -> Optional[Http403]:
        """
        The request to delete a Syllabus record is valid if:
        - The request is deleting a Syllabus in the User's Member
        - The specified Class relating to this Syllabus has no students
        """
        # The request is deleting a Syllabus in the User's Member
        if request.user.member['id'] != obj.member_id:
            return Http403(error_code='training_syllabus_delete_201')
        # The specified Class relating to this Syllabus has no students
        if Student.objects.filter(cls__syllabus=obj).exists():
            return Http403(error_code='training_syllabus_delete_202')
        return None
