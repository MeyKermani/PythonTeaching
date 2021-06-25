x = 0
if x:
    print("yes")
###################
y = []
if y:
    print(y)
###################
"""
These are always False:

constants defined to be false: None and False.

zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

empty sequences and collections: '', (), [], {}, set(), range(0)

"""


if None:
    print("hello")


x = True
y = False

# print(x)
# print(not x)
# print(y)
# print(x and y)
# print(x and not y)
# print(x or y)

"""
not has a lower priority than non-Boolean operators,
 so not a == b is interpreted as not (a == b), and a == not b is a syntax error.
"""

#(not a) == b  -> correct
#not a ==b     ->run time error not(a==b) or a!=b
#a = not b     -> syntax error


"""
Operation   Meaning

<           strictly less than

<=          less than or equal

>           strictly greater than

>=          greater than or equal

==          equal

!=          not equal

is          object identity

is not      negated object identity

"""



x = 10
print(type(x))
print(isinstance(x, int))
print(isinstance(x, float))
print(isinstance(x, str))


x = 10
print(id(x))
y = x
print(id(y))
print(x is y)
y = 5
print(x)
print(id(x))
print(id(y))


if y<x:
    print(y)



#######################################################
grade = 'A'

print("Passed" if grade in ['A','B','C'] else "Failed")
print("Gongrats!" if grade == 'A' else '')
list_ = []

print('HAVE ELEMENTS'  if list_ else "IS EMPTY" )