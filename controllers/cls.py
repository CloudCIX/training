# stdlib
from datetime import datetime
from typing import Optional, cast
# libs
from cloudcix_rest.controllers import ControllerBase
# local
from training.models import Cls, Syllabus

__all__ = [
    'ClsListController',
    'ClsCreateController',
    'ClsUpdateController',
]


class ClsListController(ControllerBase):
    """
    Validates User data used to list Class records
    """
    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make them more specific
        for this Controller
        """
        allowed_ordering = (
            'id',
            'created',
            'finish_date',
            'start_date',
            'syllabus__name',
            'trainer',
        )
        search_fields = {
            'id': ControllerBase.DEFAULT_NUMBER_FILTER_OPERATORS,
            'finish_date': ControllerBase.DEFAULT_NUMBER_FILTER_OPERATORS,
            'start_date': ControllerBase.DEFAULT_NUMBER_FILTER_OPERATORS,
            'syllabus_id': ControllerBase.DEFAULT_NUMBER_FILTER_OPERATORS,
            'syllabus__name': ControllerBase.DEFAULT_STRING_FILTER_OPERATORS,
            'trainer': ControllerBase.DEFAULT_STRING_FILTER_OPERATORS,
        }


class ClsCreateController(ControllerBase):
    """
    Validates User data used to create a new Class record
    """
    class Meta(ControllerBase.Meta):
        """
        Overrides some of the ControllerBase.Meta fields to make them more specific
        for this controller
        """
        model = Cls
        validation_order = (
            'start_date',
            'finish_date',
            'syllabus_id',
            'trainer',
        )

    def validate_start_date(self, start_date: Optional[datetime]) -> Optional[str]:
        """
        description: The date on which the Class should begin
        type: string
        """
        try:
            self.cleaned_data['start_date'] = datetime.strptime(str(start_date).split('T')[0], '%Y-%m-%d')
        except (TypeError, ValueError):
            return 'training_cls_create_101'
        return None

    def validate_finish_date(self, finish_date: Optional[datetime]) -> Optional[str]:
        """
        description: The date on which the Class should end
        type: string
        required: false
        """
        if finish_date is None:
            return None
        try:
            finish_date = datetime.strptime(str(finish_date).split('T')[0], '%Y-%m-%d')
        except (TypeError, ValueError):
            return 'training_cls_create_102'
        if 'start_date' not in self.cleaned_data:
            return None

        # Check that it's valid compared to the start_date
        if finish_date < self.cleaned_data['start_date']:
            return 'training_cls_create_103'
        self.cleaned_data['finish_date'] = finish_date
        return None

    def validate_syllabus_id(self, syllabus_id: Optional[int]) -> Optional[str]:
        """
        description: The id for the Syllabus used to make a Class
        type: integer
        """
        try:
            syllabus = Syllabus.objects.get(id=int(cast(int, syllabus_id)))
        except (ValueError, TypeError):
            # syllabus_id was not an int
            return 'training_cls_create_104'
        except Syllabus.DoesNotExist:
            return 'training_cls_create_105'
        self.cleaned_data['syllabus'] = syllabus
        return None

    def validate_trainer(self, trainer: Optional[str]) -> Optional[str]:
        """
        description: The name of the trainer for the class
        type: string
        """
        if trainer is None:
            trainer = ''
        trainer = str(trainer).strip()
        if len(trainer) == 0:
            return 'training_cls_create_106'
        if len(trainer) > self.get_field('trainer').max_length:
            return 'training_cls_create_107'
        self.cleaned_data['trainer'] = trainer
        return None


class ClsUpdateController(ControllerBase):
    """
    Validates User data used to update a new Class record
    """
    class Meta(ControllerBase.Meta):
        """
        Overrides some of the ControllerBase.Meta fields to make them more specific
        for this controller
        """
        model = Cls
        validation_order = (
            'start_date',
            'finish_date',
            'syllabus_id',
            'trainer',
        )

    def validate_start_date(self, start_date: Optional[datetime]) -> Optional[str]:
        """
        description: The date on which the Class should begin
        type: string
        """
        try:
            self.cleaned_data['start_date'] = datetime.strptime(str(start_date).split('T')[0], '%Y-%m-%d')
        except (TypeError, ValueError):
            return 'training_cls_update_101'
        return None

    def validate_finish_date(self, finish_date: Optional[datetime]) -> Optional[str]:
        """
        description: The date on which the Class should end
        type: string
        required: false
        """
        if 'start_date' not in self.cleaned_data:
            if 'start_date' not in self.errors:
                self.cleaned_data['start_date'] = self._instance.start_date
            else:
                return None
        if finish_date is None:
            self.cleaned_data['finish_date'] = None
            return None
        try:
            finish_date = datetime.strptime(str(finish_date).split('T')[0], '%Y-%m-%d')
        except (TypeError, ValueError):
            return 'training_cls_update_102'
        # Check that it's valid compared to the start_date
        if finish_date < self.cleaned_data['start_date']:
            return 'training_cls_update_103'
        self.cleaned_data['finish_date'] = finish_date
        return None

    def validate_syllabus_id(self, syllabus_id: Optional[int]) -> Optional[str]:
        """
        description: The id for the Syllabus used to make a Class
        type: integer
        """
        try:
            syllabus = Syllabus.objects.get(id=int(cast(int, syllabus_id)))
        except (ValueError, TypeError):
            # syllabus_id was not an int
            return 'training_cls_update_104'
        except Syllabus.DoesNotExist:
            return 'training_cls_update_105'

        self.cleaned_data['syllabus'] = syllabus
        return None

    def validate_trainer(self, trainer: Optional[str]) -> Optional[str]:
        """
        description: The name of the trainer for the class
        type: string
        """
        if trainer is None:
            trainer = ''
        trainer = str(trainer).strip()
        if len(trainer) == 0:
            return 'training_cls_update_106'

        if len(trainer) > self.get_field('trainer').max_length:
            return 'training_cls_update_107'

        self.cleaned_data['trainer'] = trainer
        return None
