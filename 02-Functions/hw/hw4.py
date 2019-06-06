"""
Напишите функцию modified_func, которая принимает функцию (обозначим ее func),
а также произвольный набор позиционных (назовем их fixated_args) и именованных
(назовем их fixated_kwargs) аргументов и возвращает новую функцию,
которая обладает следующими свойствами:

1.При вызове без аргументов повторяет поведение функции func, вызванной
с fixated_args и fixated_kwargs.
2.При вызове с позиционными и именованными аргументами дополняет ими
fixed_args (приписывает в конец списка fixated_args), и fixated_kwargs
(приписывает новые именованные аргументы и переопределяет значения старых)
и далее повторяет поведение func с этим новым набором аргументов.
3.Имеет __name__ вида func_<имя функции func>
4.Имеет docstring вида:

""
A func implementation of <имя функции func>
with pre-applied arguments being:
<перечисление имен и значений fixated_args и fixated_kwargs>
source_code:
   ...
""
Для того, чтобы получить имена позиционных аргументов и исходный код, советуем использовать
возможности модуля inspect.

Попробуйте применить эту функцию на написанных функциях из дз1, дз2, дз3. К функциям min, max, any() ?
"""
import itertools
import inspect
from hw1 import letters_range


def modified_func(func, *args1, **kwargs1):
    func_name = func.__name__
    fixed_args = args1
    fixed_kwargs = kwargs1
    def new_func(*args2, **kwargs2):
        new_args = (*args2,) + (*fixed_args,)
        new_kwargs = {}
        new_kwargs.update(kwargs2)
        new_kwargs.update(fixed_kwargs)
        result = func(new_args, **new_kwargs)
        return result
    print(type(func))
    if type(func) == type(min):
        code = "Sorry, this is built-in function or method and\n\
        I can't reach CPython sourcecode"
    else:
        code = inspect.getsource(func)
    new_func.__doc__ = f"A func implementation of {func_name}\n\
    with pre-applied arguments being:\n\
    {fixed_args, fixed_kwargs}\n\
    source_code:\n{code}"
    new_func.__name__ = 'func_' + str(func_name)
    return new_func

def show(*args, **kwargs):
    print()
    print(*args)
    print(kwargs)

new_function = modified_func(letters_range, 1, 2)
print(new_function.__doc__)
