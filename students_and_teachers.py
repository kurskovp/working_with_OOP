class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []


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

