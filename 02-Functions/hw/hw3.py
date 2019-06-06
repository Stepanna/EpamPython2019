"""
Напишите реализацию функции make_it_count, которая принимает в качестве
аргументов некую функцию (обозначим ее func) и имя глобальной переменной
(обозначим её counter_name), возвращая новую функцию, которая ведет себя
в точности как функция func, за тем исключением, что всякий раз при вызове
инкрементирует значение глобальной переменной с именем counter_name.
"""
counter = 0
counter_name = 'counter'

def func():
    print("Hello, world")

def make_it_count(func, count_name):
    def wrapper(*args, **kwargs):
        copy_globals = globals().items()
        for k, v in copy_globals:
            if k == count_name:
                globals()[k] += 1
        result = func(*args, **kwargs)
        return result
    return wrapper

new_f = make_it_count(func, counter_name)
new_f()
print(counter)
