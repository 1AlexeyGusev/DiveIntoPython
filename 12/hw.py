# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.


import csv

class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.isalpha() or not value[0].isupper():
            raise ValueError(f"{self.name} должен начинаться с заглавной буквы и содержать только буквы.")
        instance.__dict__[self.name] = value

class Student:
    first_name = NameDescriptor()
    last_name = NameDescriptor()
    patronymic = NameDescriptor()

    def __init__(self, first_name, last_name, patronymic, subjects_file):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        try:
            with open(subjects_file, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    subject = row[0].strip()
                    self.subjects[subject] = {'grades': [], 'tests': []}
        except FileNotFoundError:
            print(f"Файл {subjects_file} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке предметов: {e}")

    def add_grade(self, subject, grade):
        if subject in self.subjects and 2 <= grade <= 5:
            self.subjects[subject]['grades'].append(grade)
        else:
            raise ValueError("Некорректный предмет или оценка.")

    def add_test_score(self, subject, score):
        if subject in self.subjects and 0 <= score <= 100:
            self.subjects[subject]['tests'].append(score)
        else:
            raise ValueError("Некорректный предмет или результат теста.")

    def average_test_score(self, subject):
        if subject in self.subjects and self.subjects[subject]['tests']:
            return sum(self.subjects[subject]['tests']) / len(self.subjects[subject]['tests'])
        return 0.0

    def overall_average_grade(self):
        total_grades = []
        for subject in self.subjects.values():
            total_grades.extend(subject['grades'])
        if total_grades:
            return sum(total_grades) / len(total_grades)
        return 0.0

if __name__ == '__main__':
    student = Student("Иван", "Иванов", "Иванович", "subjects.csv")
    student.add_grade("Математика", 5)
    student.add_test_score("Математика", 90)
    print(student.average_test_score("Математика"))
    print(student.overall_average_grade())
