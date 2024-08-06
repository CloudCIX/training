from .cls import (
    ClsCreateController,
    ClsListController,
    ClsUpdateController,
)

from .syllabus import (
    SyllabusCreateController,
    SyllabusListController,
    SyllabusUpdateController,
)

from .student import (
    StudentCreateController,
    StudentListController,
    StudentUpdateController,
)


__all__ = [
    # Class

    'ClsCreateController',
    'ClsListController',
    'ClsUpdateController',

    # Syllabus

    'SyllabusCreateController',
    'SyllabusListController',
    'SyllabusUpdateController',

    # Student

    'StudentCreateController',
    'StudentListController',
    'StudentUpdateController',
]
