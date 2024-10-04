a = 11
a += 5
type_a = type(a)
print(f"a = {a} and its data type is {type_a}")

b = 12.5
b -= 3.1
type_b = type(b)
print(f"b = {b} and its data type is {type_b}")

c = 10
c *= 2
type_c = type(c)
print(f"c = {c} and its data type is {type_c}")

d = 12
d /= 4       # floating point division result will always be a float
type_d = type(d)
print(f"d = {d} and its data type is {type_d}")

e = 12
e //= 5      # floor division truncates to only display the integer part of the result
type_e = type(e)
print(f"e = {e} and its data type is {type_e}")

f = 10
f **= 2      # exponentiation eg: 10 x 10 10 ** 2
type_f = type(f)
print(f"f = {f} and its data type is {type_f}")

g = 12
g %= 5
type_g = type(g)  #modulus (remainder)
print(f"g = {g} and its data type is {type_g}")

