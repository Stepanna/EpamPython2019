

"""
Число Армстронга
— натуральное число,
которое в данной системе счисления равно сумме своих цифр,
возведённых в степень, равную количеству его цифр.

К примеру:

- 9 это число Армстронга, т.к. 9 = 9^1 = 9
- 10 не является подобным числом: 10 != 1^2 + 0^2 = 1
- 153 является числом Армстронга: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

### Задача

Написать функцию определения числа Армстронга в функциональном виде:
 - использовать map или другие утилиты functools,
 - задействовать анонимные функций (или использовать функцию в качестве
 аргумента)
 - не использовать циклы, предпочитая list comprehensions

 ### Пример сигнатуры и вызовов функции

 ```python
 def is_armstrong(number):
   ...

 assert is_armstrong(153) == True, 'Число Армстронга'
 assert is_armstrong(10) == False, 'Не число Армстронга'
 ```
"""


def is_armstrong(number):
    sum_in_pow = sum([int(dig)**len(str(number)) for dig in str(number)])
    return ((lambda a, x: a == x)(sum_in_pow, number))


print(is_armstrong(9))
