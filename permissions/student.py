"""
Permissions classes will use their methods to validate permissions for a
request.
These methods will raise any errors that may occurs all you have to do is
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
    def create(request: Request, obj: Syllabus) -> Optional[Http403]:
        """
        The request to create a new Student record is valid if:
        - The User creating a Student is a self-managed Member
        - The request is creating a Student in the User's Member
        """
        # The requesting User's Member is self-managed
        if not request.user.member['self_managed']:
            return Http403(error_code='training_student_create_201')

        # The request is creating a Student in the User's Member
        if obj.member_id != request.user.member['id']:
            return Http403(error_code='training_student_create_202')
        return None

    @staticmethod
    def read(request: Request, obj: Student) -> Optional[Http403]:
        """
        The request to read a Student record is valid if:
        - The request is reading a Student in the User's Member
        """
        # The request is reading a Student in the User's Member
        if obj.cls.syllabus.member_id != request.user.member['id']:
            return Http403(error_code='training_student_read_201')
        return None

    @staticmethod
    def update(request: Request, obj: Student) -> Optional[Http403]:
        """
        The request to update a Student record is valid if:
        - The request is updating a Student in the User's Member
        """
        # The request is updating a Student in the User's Member
        if obj.cls.syllabus.member_id != request.user.member['id']:
            return Http403(error_code='training_student_update_201')
        return None

    @staticmethod
    def delete(request: Request, obj: Student) -> Optional[Http403]:
        """
        The request to delete a Student record is valid if:
        - The request is deleting a Student in the User's Member
        """
        # The request is deleting a Student in the User's Member
        if obj.cls.syllabus.member_id != request.user.member['id']:
            return Http403(error_code='training_student_delete_201')
        return None
