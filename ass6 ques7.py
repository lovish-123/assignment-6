class Student:
    pass

class Marks:
    pass

# creating instances
student1 = Student()
marks1 = Marks()

# checking if instances are of the correct class
print(isinstance(student1, Student)) # True
print(isinstance(marks1, Marks)) # True

# checking if classes are subclass of object class
print(issubclass(Student, object)) # True
print(issubclass(Marks, object)) # True