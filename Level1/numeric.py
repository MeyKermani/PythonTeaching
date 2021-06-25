from math import pi
x = 10
y = 10.2

print(type(x))
print(type(y))

"""
Complex
"""
z = complex(1,2)
print(z)
print(type(z))
print(z.conjugate())



"""
Fraction
"""
from fractions import Fraction
w = Fraction(5,2)
print(w)

s = Fraction(0.125)
print(s)
print(pi)

piz = Fraction(pi)
print(piz)

a = Fraction(2,4)
print(a)

q = Fraction(1.4)
print(q)

"""
Decimal
"""
from decimal import Decimal
d = Decimal(1.4)
print(d)
