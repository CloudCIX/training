"""
 Training is a CloudCIX Application that exposes a REST API capable of managing Training records.

The Training records consist of the following elements:

- Syllabus: A Syllabus is the guide to a course and what will be expected of the student in the course.
- Class: A Syllabus may have one or several Classes. Every Class has a trainer assigned and a start and end date.
- Student: A Student is an User of CloudCIX Membership. Students can be in different Classes and the trainer of each
  Class will add notes about the Student in its training record.
"""
__version__ = '4.0.0'
