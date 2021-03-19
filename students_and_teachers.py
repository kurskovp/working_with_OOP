class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def set_lecturer_grade(self, lecturer, course, grade):
        if course in self.courses_in_progress:
            if course in lecturer.teaching_course:
                lecturer.grades[course] = grade
            else:
                print(f'Преподаватель этот курс не ведет - {course}')
        else:
            print(f'Студент не записан на данный курс, оценку лектору поставить не может - {course}')


    # def get_av_grades(self):
    #     self.add = sum(self.grades)/len(self.grades)
    #     return add

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}   \nКурсы в прцессе изучения: {self.courses_in_progress }' \
               f'\nОценки за курсы: {self.grades}'

class Mentor:
    def __init__(self, name, surname, teaching_course):
        self.name = name
        self.surname = surname
        self.teaching_course = teaching_course



class Lecturer(Mentor):
    def __init__(self,name, surname, teaching_course):
        Mentor. __init__ (self,name, surname, teaching_course)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grades} '



class Reviewer(Mentor):
    def __init__(self,name, surname, teaching_course):
        Mentor. __init__ (self,name, surname, teaching_course)

    def set_student_grade(self, student, cours, grade):
        if cours in self.teaching_course:
            if cours in student.courses_in_progress:
                student.grades[cours] = grade
            else:
                print(f'Преподаватель этот курс не должен проверять - {cours}')
        else:
            print(f'Студент не записан на данный курс - {cours}')



# Проверочный блок:

john = Student("John", "Smith", "male")
john.courses_in_progress = ["Python", "Git"]
bill = Student("Bill", "Cogan", "male")
bill.courses_in_progress = ["Python", "Biology", "Git"]
print('Студенты', sep='\n')
print(john, bill, sep='\n \n')

# print(john.courses_in_progress[1])

# print(john.gender)


rev_1 = Reviewer('Nic', 'Popov', ["Math", "Git", "Python", "Biology"])
rev_1.set_student_grade(john, 'Git', 4)
rev_1.set_student_grade(john, 'Python', 5)
rev_1.set_student_grade(bill, 'Python', 7)
rev_1.set_student_grade(bill, 'Git', 5)
rev_1.set_student_grade(john, 'Biology', 3)

# print(john.grades)

lec_1 = Lecturer("Adam", "Nolan", ["Biology", "Geom", "Python"])
lec_2 = Lecturer("Игорь", "Петров", ["Math", "Git", "Physics"])
john.set_lecturer_grade(lec_1, "Biology", 3)
john.set_lecturer_grade(lec_2, "Git", 4)
john.set_lecturer_grade(lec_1, "Python", 5)
bill.set_lecturer_grade(lec_1, "Python", 7)
bill.set_lecturer_grade(lec_2, "Git", 5)
john.set_lecturer_grade(lec_1, "Biology", 8)
print('Лекторы:')
print(lec_1, lec_2, sep='\n\n')