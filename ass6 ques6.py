def student_data(student_id, **kwargs):
    print("Student ID:", student_id)
    if 'student_name' in kwargs:
        print("Student Name:", kwargs['student_name'])
    if 'student_class' in kwargs:
        print("Student Class:", kwargs['student_class'])

student_data(123) # Student ID: 123
student_data(456, student_name="John", student_class="10th") # Student ID: 456
# Student Name: John
# Student Class: 12th