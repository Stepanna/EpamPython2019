# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

import string

def is_permutation(a: str, b: str) -> bool:
    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками
    a_letters = []
    b_letters = []
    if len(a) != len(b):
        return False
    for i in range(0, len(a)-1):
        for j in range(0, 51):
            if a[i]==string.ascii_letters[j]:
                a_letters.append(1)
            else: 
                a_letters.append(0) 
                
    for i in range(0, len(b)-1):
        for j in range(0, 51):
            if a[i]==string.ascii_letters[j]:
                b_letters.append(1)
            else: 
                b_letters.append(0) 
    
    if a_letters == b_letters:
        return True
    
    return False
                


assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')
