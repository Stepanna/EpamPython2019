"""
Напишите реализацию функции atom, которая инкапсулирует некую переменную,
предоставляя интерфейс для получения и изменения ее значения,
таким образом, что это значение нельзя было бы получить или изменить
иными способами.
Пусть функция atom принимает один аргумент, инициализирующий хранимое значение
(значение по умолчанию, в случае вызова atom без аргумента - None),
а возвращает 3 функции - get_value, set_value, process_value, delete_value,такие, что:

get_value - позволяет получить значение хранимой переменной;
set_value - позволяет установить новое значение хранимой переменной,
    возвращает его;
process_value - принимает в качестве аргументов сколько угодно функций
    и последовательно (в порядке перечисления аргументов) применяет эти функции
    к хранимой переменной, обновляя ее значение (перезаписывая получившийся
    результат) и возвращая получишееся итоговое значение.
delete_value - удаляет переменную, значение храние в ней и функции get_value,
    set_value, process_value. Если получится, то и delete_value
"""
def atom(value = None):
    def get_value():
        nonlocal value
        return value

    def set_value():
        new_value = input()
        nonlocal value
        value = new_value
        print(set_value.__module__)
        return value

    def process_value(*args):
        nonlocal value
        for func in args:
            func()
        return  value

    def delete_value():
        copy_globals = list(globals().items())
        global value
        del_f = [value, get_value, set_value, process_value, delete_value]
        for key, value in copy_globals:
            if value in del_f:
                del(globals()[key])
    # if (key == 'g_value'):
    # print(type(value))
    return get_value, set_value, process_value, delete_value


g_value, s_value, proc_value, del_value = atom(3)

del_value()
del_value
