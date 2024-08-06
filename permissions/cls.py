"""
Permissions classes will use their methods to validate permissions for a
request.
These methods will raise any errors that may occurso all you have to do is
call the method in the view
"""
# stdlib
from typing import Optional
# libs
from cloudcix_rest.exceptions import Http403
from rest_framework.request import Request
# local
from training.models import Cls, Student, Syllabus


class Permissions:
    @staticmethod
    def create(request: Request, obj: Syllabus) -> Optional[Http403]:
        """
        The request to create a new Class record is valid if:
        - The User creating a Class is a self-managed Member
        - The request is creating a Class in the User's Member
        """
        # The requesting User's Member is self-managed
        if not request.user.member['self_managed']:
            return Http403(error_code='training_cls_create_201')

        # The request is creating a Class in the User's Member
        if obj.member_id != request.user.member['id']:
            return Http403(error_code='training_cls_create_202')
        return None

    @staticmethod
    def read(request: Request, obj: Cls) -> Optional[Http403]:
        """
        The request to read a Class record is valid if:
        - The request is reading a Class in the User's Member
        """
        # The request is reading a Class in the User's Member
        if request.user.member['id'] != obj.syllabus.member_id:
            return Http403(error_code='training_cls_read_201')
        return None

    @staticmethod
    def update(request: Request, obj: Cls) -> Optional[Http403]:
        """
        The request to update a Class record is valid if:
        - The request is updating a Class in the User's Member
        """
        # The request is updating a Class in the User's Member
        if request.user.member['id'] != obj.syllabus.member_id:
            return Http403(error_code='training_cls_update_201')
        return None

    @staticmethod
    def delete(request: Request, obj: Cls) -> Optional[Http403]:
        """
        The request to delete a Class record is valid if:
        - The request is deleting a Class in the User's Member
        - There are no Students in a Class
        """
        # The request is deleting a Class in the User's Member
        if request.user.member['id'] != obj.syllabus.member_id:
            return Http403(error_code='training_cls_delete_201')
        # There are no Students in a Class
        if Student.objects.filter(cls=obj).exists():
            return Http403(error_code='training_cls_delete_202')
        return None
