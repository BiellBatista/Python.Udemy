# -*- coding: utf-8 -*-

a = 10
x = y = z = a

print(x, y, z, a)

print(x == y == z == a) # True
print(x == y == z == a == 1) # False
d = x == y == z == a == 1 # d ficcomo um type() bool
