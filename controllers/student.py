# stdlib
from typing import cast, Optional
# libs
from cloudcix.api import Membership
from cloudcix_rest.controllers import ControllerBase
# local
from training.models import Cls, Student

__all__ = [
    'StudentListController',
    'StudentCreateController',
    'StudentUpdateController',
]


class StudentListController(ControllerBase):
    """
    Validates User data used to list Student records
    """
    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make them more
        specific to this Controller
        """
        allowed_ordering = (
            'id',
            'cls_id',
            'cls__trainer',
            'created',
            'user_id',
            'cls__syllabus__name',
            'cls__start_date',
            'cls__finish_date',
        )
        search_fields = {
            'id': ControllerBase.DEFAULT_NUMBER_FILTER_OPERATORS,
            'cls_id': ControllerBase.DEFAULT_NUMBER_FILTER_OPERATORS,
            'cls__trainer': ControllerBase.DEFAULT_STRING_FILTER_OPERATORS,
            'notes': ControllerBase.DEFAULT_STRING_FILTER_OPERATORS,
            'user_id': ControllerBase.DEFAULT_NUMBER_FILTER_OPERATORS,
            'cls__syllabus__name': ControllerBase.DEFAULT_STRING_FILTER_OPERATORS,
        }


class StudentCreateController(ControllerBase):
    """
    Validates User data used to create a new Student record
    """
    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make them more specific for this controller
        """
        model = Student
        validation_order = (
            'cls_id',
            'user_id',
            'notes',
        )

    def validate_cls_id(self, cls_id: Optional[int]) -> Optional[str]:
        """
        description: The Class id associated with a Student
        type: integer
        """
        try:
            cls = Cls.objects.get(id=int(cast(int, cls_id)))
        except (ValueError, TypeError):
            # cls_id was not an int
            return 'training_student_create_101'
        except Cls.DoesNotExist:
            return 'training_student_create_102'
        self.cleaned_data['cls'] = cls
        return None

    def validate_notes(self, notes: Optional[str]) -> Optional[str]:
        """
        description: notes associated with a student
        type: string
        required: false
        """
        self.cleaned_data['notes'] = str(notes).strip() if notes else ''
        return None

    def validate_user_id(self, user_id: Optional[int]) -> Optional[str]:
        """
        description: The user_id associated with a Student
        type: integer
        """
        try:
            user_id = int(cast(int, user_id))
            if user_id is None or user_id <= 0:
                raise ValueError
        except(TypeError, ValueError):
            return 'training_student_create_103'
        try:
            response = Membership.user.read(
                token=self.request.auth,
                pk=user_id,
                span=self.span,
            )
            if response.status_code != 200:
                raise ValueError
        except ValueError:
            return 'training_student_create_104'
        self.cleaned_data['user_id'] = user_id
        return None


class StudentUpdateController(ControllerBase):
    """
    Validates User data used to update a Student record
    """
    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make the more specific for this Controller
        """
        model = Student
        validation_order = (
            'cls_id',
            'user_id',
            'notes',
        )

    def validate_cls_id(self, cls_id: Optional[int]) -> Optional[str]:
        """
        description: The Class id associated with a Student
        type: integer
        """
        try:
            cls = Cls.objects.get(id=int(cast(int, cls_id)))
        except (ValueError, TypeError):
            # cls_id was not an int
            return 'training_student_update_101'
        except Cls.DoesNotExist:
            return 'training_student_update_102'
        self.cleaned_data['cls'] = cls
        return None

    def validate_notes(self, notes):
        """
        description: notes associated with a student
        type: string
        required: false
        """
        self.cleaned_data['notes'] = str(notes).strip() if notes else ''
        return None

    def validate_user_id(self, user_id: Optional[int]) -> Optional[str]:
        """
        description: The user_id associated with a Student
        type: integer
        """
        try:
            user = int(cast(int, user_id))
            if user is None or user <= 0:
                raise ValueError
        except(TypeError, ValueError):
            return 'training_student_update_103'
        try:
            response = Membership.user.read(
                token=self.request.auth,
                pk=user,
                span=self.span,
            )
            if response.status_code != 200:
                raise ValueError
        except ValueError:
            return 'training_student_update_104'
        self.cleaned_data['user_id'] = user
        return None
