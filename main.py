class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade_hw(self, grade):
        all_list_grades = []
        for course in self.grades:
            all_list_grades += self.grades[course]
        return round(sum(all_list_grades) / len(all_list_grades), 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_grade_hw(self.grades) < other.average_grade_hw(other.grades)

    def __str__(self):
        courses_all_prgs = ', '
        finished_crs = ', '
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: " \
              f"{self.average_grade_hw(self.grades)}\n" \
              f"Курсы в процессе изучения: {courses_all_prgs.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {finished_crs.join(self.finished_courses)}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades_lec(self, self_grades):
        all_list_grades = []
        for course in self.grades:
            all_list_grades += self.grades[course]
        return round(sum(all_list_grades) / len(all_list_grades), 2)
    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Not a Lecturer')
            return
        return self.average_grades_lec(self.grades) < other.average_grades_lec(self.grades)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades_lec(self.grades)}"
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res
# Студенты
Ivan = Student('Ivan', 'Ivanov', 'Man')
Ivan.courses_in_progress += ['Python', 'Git']
Ivan.finished_courses += ['Вводный курс']

Anna = Student('Anna', 'Petrova', 'Woman')
Anna.courses_in_progress += ['Python', 'Git']
Anna.finished_courses += ['Вводный курс']

# Лекторы
Johann = Lecturer('Johann', 'Bach')
Johann.courses_attached += ['Python', 'Git']

Michael = Lecturer('Michael', 'Smith')
Michael.courses_attached += ['Python', 'Git']

# Проверяющие эксперты
Dmitriy = Reviewer('Dmitriy', 'Sidorov')
Dmitriy.courses_attached += ['Python', 'Git']
Oleg = Reviewer('Oleg', 'Syomin')
Oleg.courses_attached += ['Python', 'Git']

# Оценки студентам
Dmitriy.rate_hw(Ivan, 'Python', 10)
Oleg.rate_hw(Ivan, 'Python', 9)
Dmitriy.rate_hw(Ivan, 'Git', 8)
Oleg.rate_hw(Ivan, 'Git', 9)
Dmitriy.rate_hw(Anna, 'Python', 10)
Oleg.rate_hw(Anna, 'Python', 10)
Dmitriy.rate_hw(Anna, 'Git', 9)
Oleg.rate_hw(Anna, 'Git', 10)

#Оценки Лекторам
Ivan.rate_lecture(Johann, 'Python', 9)
Anna.rate_lecture(Johann, 'Python', 10)
Ivan.rate_lecture(Johann, 'Git', 7)
Anna.rate_lecture(Johann, 'Git', 10)
Ivan.rate_lecture(Michael, 'Python', 10)
Anna.rate_lecture(Michael, 'Python', 10)
Ivan.rate_lecture(Michael, 'Git', 10)
Anna.rate_lecture(Michael, 'Git', 10)

print(f'{Ivan}\n')
print(f'{Anna}\n')
print(f'{Johann}\n')
print(f'{Michael}\n')
print(f'{Dmitriy}\n')
print(f'{Oleg}\n')

full_list_student = [Ivan, Anna]
full_list_lecturer = [Johann, Michael]

def average_any_course_st(class_list, course):
    list_grade = []
    for student in class_list:
        for courses in student.grades:
            if courses == course:
                list_grade += student.grades[course]
    return print(f"Средний бал студентов по курсу  {course}: {round(sum(list_grade) / len(list_grade), 2)}\n")

def average_any_course_lec(class_list, course):
    list_grade = []
    for lecturer in class_list:
        for courses in lecturer.grades:
            if courses == course:
                list_grade += lecturer.grades[course]
    return print(f"Средний бал лекторов по курсу  {course}: {round(sum(list_grade) / len(list_grade), 2)}\n")

# print(Johann.name, Johann.grades)
# print(Michael.name, Michael.grades)
average_any_course_lec(full_list_lecturer, 'Python')
average_any_course_lec(full_list_lecturer, 'Git')
# print(Ivan.name, Ivan.grades)
# print(Anna.name, Anna.grades)
average_any_course_st(full_list_student, 'Python')
average_any_course_st(full_list_student, 'Git')

print(Johann > Michael)





