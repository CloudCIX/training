"""
error codes for all the methods in Cls
"""
# List
training_cls_list_001 = (
    'One or more of the sent search fields contains invalid values. Please check the sent parameters and ensure they '
    'match the required patterns.'
)

# Create
training_cls_create_101 = (
    'The "start_date" parameter is invalid. "start_date" is required and must be a date in ISO format.'
)
training_cls_create_102 = (
    'The "finish_date" parameter is invalid. "finish_date" must be a date in ISO format.'
)
training_cls_create_103 = (
    'The "finish_date" parameter is invalid. "finish_date" cannot be before the specified "start_date".'
)
training_cls_create_104 = 'The "syllabus_id" parameter is invalid. "syllabus_id" is required and must be an integer.'
training_cls_create_105 = 'The "syllabus_id" parameter is invalid. "syllabus_id" must belong to a valid Syllabus.'
training_cls_create_106 = 'The "trainer" parameter is invalid. "trainer" is required and must be a string.'
training_cls_create_107 = 'The "trainer" parameter is invalid. "trainer" cannot be longer than 50 characters.'
training_cls_create_201 = 'You do not have permission to make this request. Your Member must be self-managed.'
training_cls_create_202 = (
    'You do not have permission to execute this method. You can only create a Class in your Member.'
)

# Read
training_cls_read_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Class record.'
training_cls_read_201 = (
    'You do not have permission to execute this method. You can only read a Class in your Member.'
)

# Update
training_cls_update_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Class record.'
training_cls_update_101 = (
    'The "start_date" parameter is invalid. "start_date" is required and must be a date in ISO format.'
)
training_cls_update_102 = (
    'The "finish_date" parameter is invalid. "finish_date" is required and must be a date in ISO format.'
)
training_cls_update_103 = (
    'The "finish_date" parameter is invalid. "finish_date" cannot be before the specified "start_date".'
)
training_cls_update_104 = 'The "syllabus_id" parameter is invalid. "syllabus_id" is required and must be an integer.'
training_cls_update_105 = 'The "syllabus_id" parameter is invalid. "syllabus_id" must belong to a valid Syllabus.'
training_cls_update_106 = 'The "trainer" parameter is invalid. "trainer" is required and must be a string.'
training_cls_update_107 = 'The "trainer" parameter is invalid. "trainer" cannot be longer than 50 characters.'
training_cls_update_201 = (
    'You do not have permission to execute this method. You can only update a Class in your Member.'
)

# Delete
training_cls_delete_001 = 'The "pk" path parameter is invalid. "pk" must belong to a valid Class record.'
training_cls_delete_201 = (
    'You do not have permission to execute this method. You can only delete a Class in your Member.'
)
training_cls_delete_202 = 'You do not have permission to make this request. The specified Class has Students in it.'
