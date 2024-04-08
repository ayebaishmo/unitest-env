import random
'''
This file contains two classes one 
is parent the other is child
'''
class Student:
    """
    This is function doc string
    """
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no

    '''
    This is function doc string
    '''

    def dorm(self, dorm_no):
        self.dorm_no = dorm_no
        return dorm_no
    
class BloomTechStudent(Student):

    def __init__(self, name, id_no, course):
        super().__init__(name, id_no)
        self.course = course
    
    def __repr__(self):
        return f'''My name is {self.name} attarched to {self.id_no} my course is {self.course}'''


def student_generator():
    names = ['Ishmael', 'Priscilla', 'Josh', 'Drake', 'Tamara', 'Eddy', 'Hush']
    id_nos = ['fdfd4324', 'fsfs4342', 'rerwr432', 'rerwerw45', 'rwrwr325', 'uyru6866', '5757bgjh']
    courses = ['Data science', 'Backend', 'Frontend']
    students = []

    for _ in range(30):
        name = random.choice(names)
        id_no = random.choice(id_nos)
        course = random.choice(courses)
        student = BloomTechStudent(name, id_no, course)
        students.append(student)
    return students

BloomTechStudent = student_generator()
if __name__ == "__main__":
    for student in BloomTechStudent:
        print(f"Name: {student.name}, id no: {student.id_no}, course: {student.course}")