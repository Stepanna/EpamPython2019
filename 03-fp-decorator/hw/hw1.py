from functools import reduce


"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
[a*b*c for a in range(1, 700) for b in range(1, 700) for c in range(1, 700)
 if a**2+b**2 == c**2 and a+b+c == 1000][0]

"""Out[13]: 31875000"""

"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""
(sum([x for x in range(1, 101)]))**2 - sum([x**2 for x in range(1, 101)])
"""25164150"""

"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
sum([x**x for x in range(1, 1001)]) % 10000000000
"""9110846700"""

"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from1to5 = [str(i+1)[j-1] if j else str(i)[0] for i, j in
            zip([((10**(n-1)-1) +
                  ((10**n - 9*reduce((lambda a, x: (a + x*(10**(x-1)))),
                                     [x for x in range(1, n) or [0]]))//n))
                 for n in [1, 2, 3, 4, 5, 6]],
                [((10**n -
                   9*reduce((lambda a, x: (a + x*(10**(x-1)))),
                            [x for x in range(1, n) or [0]])) % n)
                    for n in [1, 2, 3, 4, 5, 6]])]
print(''.join(['0', *from1to5]))
"""153721"""
