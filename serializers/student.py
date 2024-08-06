# libs
import serpy
# local
from .cls import ClsSerializer


class StudentSerializer(serpy.Serializer):
    """
    cls:
        $ref: '#/components/schemas/Cls'
    id:
        description: The id of the Student
        type: integer
    notes:
        description: The notes associated with the Student
        type: string
    user_id:
        description: The id of the User
        type: integer
    uri:
        description: |
            The absolute URL of the Student that can be used to perform 'Read', 'Update' and Delete' Operations on it
        type: string
    """
    cls = ClsSerializer(required=False)
    id = serpy.Field()
    notes = serpy.Field()
    uri = serpy.Field(attr='get_absolute_url', call=True)
    user_id = serpy.Field()
