# libs
import serpy


class SyllabusSerializer(serpy.Serializer):
    """
    description:
        description: The description of the Syllabus
        type: string
    id:
        description: The id of the Syllabus
        type: integer
    member_id:
        description: The member_id associated with the Syllabus
        type: integer
    name:
        description: The name of the Syllabus
        type: string
    uri:
        description: |
            The absolute URL of the Syllabus that can be used to perform 'Read', 'Update' and Delete' Operations on it.
        type: string
    """
    description = serpy.Field()
    id = serpy.Field()
    member_id = serpy.Field()
    name = serpy.Field()
    uri = serpy.Field(attr='get_absolute_url', call=True)
