# libs
import serpy
# local
from .syllabus import SyllabusSerializer


class ClsSerializer(serpy.Serializer):
    """
    finish_date:
        description: The finishing date of the Class
        type: string
    id:
        description: The id of the Class
        type: integer
    start_date:
        description: The starting date of the Class
        type: string
    syllabus:
        $ref: '#/components/schemas/Syllabus'
    trainer:
        description: The trainer for the Class
        type: string
    uri:
        description: |
            The absolute URL of the Class that can be used to perform 'Read', 'Update' and Delete' Operations on it
        type: string
    """
    finish_date = serpy.Field()
    id = serpy.Field()
    start_date = serpy.Field()
    syllabus = SyllabusSerializer(required=False)
    trainer = serpy.Field()
    uri = serpy.Field(attr='get_absolute_url', call=True)
