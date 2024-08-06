"""
Error codes for all of the methods in Syllabus
"""
# List
training_syllabus_list_001 = (
    'One or more of the sent search fields contains invalid values. Please check the sent parameters and ensure they '
    'match the required patterns.'
)

# Create
training_syllabus_create_101 = 'The "name" parameter is invalid. "name" is required and must be a string.'
training_syllabus_create_102 = 'The "name" parameter is invalid. "name" cannot be longer than 50 characters.'
training_syllabus_create_103 = 'The "name" parameter is invalid. A Syllabus with that name already exists.'
training_syllabus_create_201 = 'You do not have permission to make this request. Your Member must be self-managed.'

# Read
training_syllabus_read_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Syllabus record.'
training_syllabus_read_201 = (
    'You do not have permission to execute this method. You can only read a Syllabus for your Member.'
)

# Update
training_syllabus_update_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Syllabus record.'
training_syllabus_update_101 = 'The "name" parameter is invalid. "name" is required and must be a string.'
training_syllabus_update_102 = 'The "name" parameter is invalid. "name" cannot be longer than 50 characters.'
training_syllabus_update_103 = 'The "name" parameter is invalid. A Syllabus with that name already exists.'
training_syllabus_update_201 = (
    'You do not have permission to execute this method. You can only update a Syllabus in your Member.'
)

# Delete
training_syllabus_delete_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Syllabus record.'
training_syllabus_delete_201 = (
    'You do not have permission to execute this method. You can only delete a Syllabus in your Member.'
)
training_syllabus_delete_202 = (
    'You do not have permission to execute this method. The specified Syllabus has a Class with students '
    'assigned to it.'
)
