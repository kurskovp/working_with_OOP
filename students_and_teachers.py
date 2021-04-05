class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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

    def get_average(self):
        average = 0
        for grade in self.grades:
            average += grade
        grades_count = len(self.grades)
        if grades_count:
            return average / grades_count

    def __str__(self):
        result = 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname
        result += 'Средняя оценка за домашнии задания: ' + self.get_average()
        result += 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress)
        result += 'Завершенные курсы: ' + ', '.join(self.finished_courses)
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
        super(name, surname).__init__()
        self.grades = {}

    def get_average(self):
        average = 0
        for grade in self.grades:
            average += grade
        grades_count = len(self.grades)
        if grades_count:
            return average / grades_count

    def __str__(self):
        result = 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname
        result += 'Средняя оценка за лекции: ' + self.get_average()
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
        super(name, surname).__init__()

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
        result += 'Фамилия: ' + self.surname
        return result


#
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)