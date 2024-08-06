# libs
from django.urls import path
# local
from . import views

urlpatterns = [
    # Class
    path(
        'class/',
        views.ClsCollection.as_view(),
        name='cls_collection',
    ),

    path(
        'class/<int:pk>/',
        views.ClsResource.as_view(),
        name='cls_resource',
    ),

    # Student
    path(
        'student/',
        views.StudentCollection.as_view(),
        name='student_collection',
    ),

    path(
        'student/<int:pk>/',
        views.StudentResource.as_view(),
        name='student_resource',
    ),

    # Syllabus
    path(
        'syllabus/',
        views.SyllabusCollection.as_view(),
        name='syllabus_collection',
    ),

    path(
        'syllabus/<int:pk>/',
        views.SyllabusResource.as_view(),
        name='syllabus_resource',
    ),
]
