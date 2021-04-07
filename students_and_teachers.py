class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = list()
        self.courses_in_progress = list()
        self.grades = dict()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade > 10:
                grade = 10
            elif grade < 1:
                grade = 1
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average(self, course=None):
        grades_count = 0
        average = 0
        if course:
            if course in self.grades:
                for grade in self.grades[course]:
                    grades_count += 1
                    average += grade
            if grades_count:
                return average / grades_count
        else:
            for course in self.grades:
                for grade in self.grades[course]:
                    grades_count += 1
                    average += grade
            if grades_count:
                return average / grades_count
        return average

    def __str__(self):
        result = 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname + '\n'
        result += 'Средняя оценка за домашние задание: ' + str(self.get_average()) + '\n'
        result += 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + '\n'
        result += 'Завершенные курсы: ' + ', '.join(self.finished_courses) + '\n'
        return result

    def __lt__(self, other):
        return self.get_average() < other.get_average()

    def __le__(self, other):
        return self.get_average() <= other.get_average()

    def __gt__(self, other):
        return self.get_average() > other.get_average()

    def __ge__(self, other):
        return self.get_average() >= other.get_average()

    def __eq__(self, other):
        return self.get_average() == other.get_average()

    def __ne__(self, other):
        return self.get_average() != other.get_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average(self, course=None):
        grades_count = 0
        average = 0
        if course:
            if course in self.grades:
                for grade in self.grades[course]:
                    grades_count += 1
                    average += grade
            if grades_count:
                return average / grades_count
        else:
            for course in self.grades:
                for grade in self.grades[course]:
                    grades_count += 1
                    average += grade
            if grades_count:
                return average / grades_count
        return average

    def __str__(self):
        result = 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname + '\n'
        result += 'Закрепленные лекции: ' + ', '.join(self.courses_attached) + '\n'
        result += 'Средняя оценка за лекции: ' + str(self.get_average()) + '\n'
        return result

    def __lt__(self, other):
        return self.get_average() < other.get_average()

    def __le__(self, other):
        return self.get_average() <= other.get_average()

    def __gt__(self, other):
        return self.get_average() > other.get_average()

    def __ge__(self, other):
        return self.get_average() >= other.get_average()

    def __eq__(self, other):
        return self.get_average() == other.get_average()

    def __ne__(self, other):
        return self.get_average() != other.get_average()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade > 10:
                grade = 10
            elif grade < 1:
                grade = 1
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname + '\n'
        return result


#
def get_averages(instances, course):
    averages_count = 0
    average = 0
    for instance in instances:
        averages_count += 1
        average += instance.get_average(course)
    if averages_count:
        return average / averages_count
    return average


def students_average(students, course):
    return get_averages(students, course)


def lecturers_average(lecturers, course):
    return get_averages(lecturers, course)


s = list()
s.append(Student('Петр', 'Александров', 'м'))
s.append(Student('Александра', 'Петрова', 'ж'))

l = list()
l.append(Lecturer('Александр', 'Пушкин'))
l.append(Lecturer('Дмитрий', 'Менделеев'))

r = list()
r.append(Reviewer('Владимир', 'Путин'))
r.append(Reviewer('Дмитрий', 'Медведев'))

s[0].courses_in_progress.append('Литература')
s[0].courses_in_progress.append('Химия')
s[0].finished_courses.append('Математика')

s[1].courses_in_progress.append('Литература')
s[1].courses_in_progress.append('Химия')
s[1].finished_courses.append('Математика')

l[0].courses_attached.append('Литература')
l[1].courses_attached.append('Химия')

r[0].courses_attached.append('Литература')
r[0].courses_attached.append('Химия')
r[1].courses_attached.append('Литература')
r[1].courses_attached.append('Химия')

s[0].rate_lecturer(l[0], 'Литература', 10)
s[0].rate_lecturer(l[1], 'Химия', 9)

s[1].rate_lecturer(l[0], 'Литература', 9)
s[1].rate_lecturer(l[1], 'Химия', 8)

r[0].rate_student(s[0], 'Литература', 5)
r[0].rate_student(s[1], 'Химия', 4)

r[1].rate_student(s[0], 'Химия', 2)
r[1].rate_student(s[1], 'Литература', 3)

print(s[0].grades)
print(s[1].grades)

print(*s, sep='\n')
print(*l, sep='\n')
print(*r, sep='\n')

print('Средняя оценка студентов по литературе:', students_average(s, 'Литература'))
print('Средняя оценка студентов по химии:', students_average(s, 'Химия'))
print('Средняя оценка лекторов по литературе:', lecturers_average(l, 'Литература'))
print('Средняя оценка лекторов по химии:', lecturers_average(l, 'Химия'))

print('студент 1 <  студент 2:', s[0] < s[1])
print('студент 1 <= студент 2:', s[0] <= s[1])
print('студент 1 >  студент 2:', s[0] > s[1])
print('студент 1 >= студент 2:', s[0] >= s[1])
print('студент 1 == студент 2:', s[0] == s[1])
print('студент 1 != студент 2:', s[0] != s[1])

print('лектор 1 <  лектор 2:', s[0] < s[1])
print('лектор 1 <= лектор 2:', s[0] <= s[1])
print('лектор 1 >  лектор 2:', s[0] > s[1])
print('лектор 1 >= лектор 2:', s[0] >= s[1])
print('лектор 1 == лектор 2:', s[0] == s[1])
print('лектор 1 != лектор 2:', s[0] != s[1])