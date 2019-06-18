import datetime
from collections import defaultdict


class Homework:

    def __init__(self, text, deadline):
        self.created = datetime.datetime.now()
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)

    def is_active(self):
        if datetime.datetime.now() < (self.created + self.deadline):
            return True
        else:
            return False


class Student:

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError('You are late')
        return None


class Teacher(Student):
    homework_done = defaultdict(Homework)

    def create_homework(self, text, deadline):
        return Homework(text, deadline)

    def check_homework(self, hw_result):
        if len(hw_result.solution) > 5:
            self.homework_done[hw_result.task] = hw_result.solution
            return True
        return False

    @staticmethod
    def reset_results(homework=None):
        if homework:
            del Teacher.homework_done[homework]
            return None
        del Teacher.homework_done
        return None


class HomeworkResult:

    def __init__(self, author, given_task, solution):
        if not isinstance(given_task, Homework):
            raise TypeError('You gave not a Homework object')
        self.solution = solution
        self.author = author
        self.task = given_task
        self.created = datetime.datetime.now()


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
