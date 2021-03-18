class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []

    def set_lecturer_dradegra(self, lecturer, course, grade):
        if course in self.courses_in_progress:
            if course in lecturer.teaching_course:
                lecturer.grades[course] = grade
            else:
                print(f'Преподаватель этот курс не ведёт - {course}')
        else:
            print(f'Студент не записан на данный курс, оценку лектору поставить не'
                  f'может - {course}')


class Mentor:
    def __init__(self, name, surname, teaching_course):
        self.name = name
        self.surname = surname
        self.teaching_course = teaching_course


class Lecturer(Mentor):
    def __init__(self, name, surname, teaching_course):
        Mentor. __init__ (self, name, surname, teaching_course)
        self.grades = []

class Reviewer(Mentor):
    def __init__(self, name, surname, teaching_course):
        Mentor. __init__ (self, name, surname, teaching_course)

    def set_student_grade(self, student, course, grade):
        if course in student.courses_in_progress:
            if course in self.teaching_course:
                student.grades[course] = grade
            else:
                print(f'Преподаватель этот курс не должен проверять - {course}')
        else:
            print(f'Студент не записан на данный курс - {course}')

