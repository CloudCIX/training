"""
Management of Students
"""
# libs
from cloudcix_rest.exceptions import Http400, Http404
from cloudcix_rest.views import APIView
from datetime import datetime
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
# local
from training.controllers import (
    StudentCreateController,
    StudentListController,
    StudentUpdateController,
)
from training.models import Student
from training.permissions.student import Permissions
from training.serializers import StudentSerializer

__all__ = [
    'StudentCollection',
    'StudentResource',
]


class StudentCollection(APIView):
    """
    Handles methods regarding Student records that do not require an id to be specified, i.e. list, create
    """
    def get(self, request: Request) -> Response:
        """
        summary: Retrieve a list of Student records

        description: |
            Retrieve a list of the Syllabus records for the requesting User's Member.

        responses:
            200:
                description: A list of the department records, filtered and ordered by the User
            400: {}
        """
        tracer = settings.TRACER

        with tracer.start_span('validating_controller', child_of=request.span) as span:
            controller = StudentListController(data=request.GET, request=request, span=span)
            controller.is_valid()

        with tracer.start_span('get_objects', child_of=request.span):
            try:
                objs = Student.objects.filter(
                    cls__syllabus__member_id=request.user.member['id'],
                    **controller.cleaned_data['search'],
                ).exclude(
                    **controller.cleaned_data['exclude'],
                ).order_by(
                    controller.cleaned_data['order'],
                )
            except (ValueError, ValidationError):
                return Http400(error_code='training_student_list_001')

        with tracer.start_span('generating_metadata', child_of=request.span):
            limit = controller.cleaned_data['limit']
            order = controller.cleaned_data['order']
            page = controller.cleaned_data['page']
            total_records = objs.count()
            warnings = controller.warnings
            metadata = {
                'limit': limit,
                'order': order,
                'page': page,
                'total_records': total_records,
                'warnings': warnings,
            }
            objs = objs[page * limit:(page + 1) * limit]

        with tracer.start_span('serializing_data', child_of=request.span) as span:
            span.set_tag('num_objects', objs.count())
            data = StudentSerializer(instance=objs, many=True).data

        return Response({'content': data, '_metadata': metadata})

    def post(self, request: Request) -> Response:
        """
        summary: Create a new Student record

        description: |
            Create a new Student record in the requesting User's Member, using the data supplied by the User.

        responses:
            201:
                description: Student record was created successfully
            400: {}
            403: {}
        """
        tracer = settings.TRACER

        with tracer.start_span('validating_controller', child_of=request.span) as span:
            controller = StudentCreateController(data=request.data, request=request, span=span)
            if not controller.is_valid():
                return Http400(errors=controller.errors)

        with tracer.start_span('checking_permissions', child_of=request.span):
            err = Permissions.create(request, controller.instance.cls.syllabus)
            if err is not None:
                return err

        with tracer.start_span('saving_object', child_of=request.span):
            controller.instance.save()

        with tracer.start_span('serializing_data', child_of=request.span):
            data = StudentSerializer(instance=controller.instance).data

        return Response({'content': data}, status=status.HTTP_201_CREATED)


class StudentResource(APIView):
    """
    Handles methods regarding Student records that do require an id to be specified, i.e. read, update, delete
    """
    def get(self, request: Request, pk: int) -> Response:
        """
        summary: Read the details of a specified Student record

        description: |
            Attempt to read a Student record in the requesting User's Member by the given 'pk', returning a 404 if
            it does not exist

        path_params:
            pk:
                description: The id of the Student record to be read
                type: integer

        responses:
            200:
                description: Student record was read successfully
            403: {}
            404: {}
        """
        tracer = settings.TRACER

        with tracer.start_span('retrieving_student_object', child_of=request.span):
            try:
                obj = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Http404(error_code='training_student_read_001')

        with tracer.start_span('checking_permissions', child_of=request.span):
            err = Permissions.read(request, obj)
            if err is not None:
                return err

        with tracer.start_span('serializing_data', child_of=request.span):
            data = StudentSerializer(instance=obj).data

        return Response({'content': data}, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, partial: bool = False) -> Response:
        """
        summary: Update the details of a specified Syllabus record

        description:
            Attempt to update a Student record in the requesting User's Member by the given 'pk'. returning a 404 if
            it does not exist

        path_params:
            pk:
                description: The id of the Student record to be updated
                type: integer

        responses:
            200:
                description: Student record was updated successfully
            400: {}
            403: {}
            404: {}
        """

        tracer = settings.TRACER

        with tracer.start_span('retrieving_student_object', child_of=request.span):
            try:
                obj = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Http404(error_code='training_student_update_001')

        with tracer.start_span('checking_permissions', child_of=request.span):
            err = Permissions.update(request, obj)
            if err is not None:
                return err

        with tracer.start_span('validating_controller', child_of=request.span) as span:
            controller = StudentUpdateController(
                data=request.data,
                instance=obj,
                partial=partial,
                request=request,
                span=span,
            )
            if not controller.is_valid():
                return Http400(errors=controller.errors)

        with tracer.start_span('saving_object', child_of=request.span):
            controller.instance.save()

        with tracer.start_span('serializing_data', child_of=request.span):
            data = StudentSerializer(instance=controller.instance).data

        return Response({'content': data}, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        """
        Attempt to partially update a Student record
        """
        return self.put(request, pk, True)

    def delete(self, request: Request, pk: int) -> Response:
        """
        summary: Delete a specified Student record

        description: |
            Attempt to delete a Student record in the requesting User's Member by the given 'pk', returning a 404 if
            it does not exist

        path_params:
            pk:
                description: The id of the Student record to delete
                type: integer

        responses:
            204:
                description: Syllabus record was deleted successfully
            403: {}
            404: {}
        """
        tracer = settings.TRACER

        with tracer.start_span('retrieving_student_object', child_of=request.span):
            try:
                obj = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Http404(error_code='training_student_delete_001')

        with tracer.start_span('checking_permissions', child_of=request.span):
            err = Permissions.delete(request, obj)
            if err is not None:
                return err

        with tracer.start_span('saving_object', child_of=request.span):
            obj.deleted = datetime.now()
            obj.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
