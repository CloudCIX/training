# stdlib
from typing import Optional
# libs
from cloudcix_rest.controllers import ControllerBase
# local
from training.models import Syllabus


class SyllabusListController(ControllerBase):
    """
    Validates user data used to list Syllabus records
    """
    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make them more specific for this Controller
        """
        allowed_ordering = (
            'id',
            'created',
            'name',
        )
        search_fields = {
            'id': ControllerBase.DEFAULT_NUMBER_FILTER_OPERATORS,
            'name': ControllerBase.DEFAULT_STRING_FILTER_OPERATORS,
        }


class SyllabusCreateController(ControllerBase):
    """
    Validates User data used to create a new Syllabus record
    """
    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make them more specific for this Controller
        """
        model = Syllabus
        validation_order = (
            'description',
            'name',
        )

    def validate_description(self, description: Optional[str]) -> Optional[str]:
        """
        description: Description of the Syllabus
        type: string
        required: false
        """
        self.cleaned_data['description'] = str(description).strip() \
            if description else ''
        return None

    def validate_name(self, name: Optional[str]) -> Optional[str]:
        """
        description: The name of the Syllabus
        type: string
        """
        if name is None:
            name = ''
        name = str(name).strip()
        if len(name) == 0:
            return 'training_syllabus_create_101'
        if len(name) > self.get_field('name').max_length:
            return 'training_syllabus_create_102'
        self.cleaned_data['name'] = name
        syllabus = Syllabus.objects.filter(
            name=name,
            member_id=self.request.user.member['id'],
        )
        if syllabus.exists():
            return 'training_syllabus_create_103'
        self.cleaned_data['name'] = name
        return None


class SyllabusUpdateController(ControllerBase):
    """
    Validates User data used to update a Syllabus
    """
    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make them more specific for this Controller
        """
        model = Syllabus
        validation_order = (
            'description',
            'name',
        )

    def validate_description(self, description: Optional[str]) -> Optional[str]:
        """
        description: Description of the Syllabus
        type: string
        required: false
        """
        self.cleaned_data['description'] = str(description).strip() \
            if description else ''
        return None

    def validate_name(self, name: Optional[str]) -> Optional[str]:
        """
        description: The name of the Syllabus
        type: string
        """
        if name is None:
            name = ''
        name = str(name).strip()
        if len(name) == 0:
            return 'training_syllabus_update_101'
        if len(name) > self.get_field('name').max_length:
            return 'training_syllabus_update_102'

        syllabus = Syllabus.objects.filter(
            name=name,
            member_id=self.request.user.member['id'],
        ).exclude(
            pk=self._instance.pk,
        )
        if syllabus.exists():
            return 'training_syllabus_update_103'
        self.cleaned_data['name'] = name
        return None
