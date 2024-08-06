"""
Error Codes for all of the Methods in the Department Service
"""
# List
training_student_list_001 = (
    'One or more of the sent search fields contains invalid values. Please check the sent parameters and ensure they '
    'match the required patterns.'
)

# Create
training_student_create_101 = 'The "cls_id" parameter is invalid. "cls_id" is required and must be an integer'
training_student_create_102 = 'The "cls_id" parameter is invalid. "cls_id" must belong to a valid Class.'
training_student_create_103 = 'The "user_id" parameter is invalid. "user_id" is required and must be an integer.'
training_student_create_104 = 'The "user_id" parameter is invalid. You do not have permission to read this record.'
training_student_create_201 = 'You do not have permission to make this request. Your Member must be self-managed.'
training_student_create_202 = (
    'You do not have permission to execute this method. You can only create a Student in your Member.'
)

# Read
training_student_read_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Student record.'
training_student_read_201 = (
    'You do not have permission to execute this method. You can only read a Student in your Member.'
)

# Update
training_student_update_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Student record.'
training_student_update_101 = 'The "cls_id" parameter is invalid. "cls_id" is required and must be an integer.'
training_student_update_102 = 'The "cls_id" parameter is invalid. "cls_id" must belong to a valid Class.'
training_student_update_103 = 'The "user_id" parameter is invalid. "user_id" is required and must be an integer.'
training_student_update_104 = 'The "user_id" parameter is invalid. You do not have permission to read this record.'
training_student_update_201 = (
    'You do not have permission to execute this method. You can only update a Student in your Member.'
)

# Delete
training_student_delete_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Class record.'
training_student_delete_201 = (
    'You do not have permission to execute this method. You can only delete a Student from a Syllabus in your Member.'
)
