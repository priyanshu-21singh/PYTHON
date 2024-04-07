# class Student:
#     def __init__(self, enrollment_id, subject, hobby):
#         self.enrollment_id = enrollment_id
#         self.subject = subject
#         self.hobby = hobby

    


# student1 = Student(enrollment_id="12345", subject="Mathematics", hobby="Reading")


# print(student1)



# WE CAN ONLY USE __INIT__ CAN HAVE MORE THAN ONE . LAST INIT IS PERIOTITZE THEREFORE ONLY USE
# ONE INIT IN PYTHON CLASS.
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        print("Coordinates: ({self.x**2}, {self.y}, {self.z})")


point1 = Point(x=1, y=2, z=3)


point1.sqSum()
