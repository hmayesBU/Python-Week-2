a = 11
b = 5
result = a < b
type_result = type(result)
print(f"result = {result} and its data type is {type_result}")

x = 10
x = 14
print(x)

a = "Hello, I am here"
a = "Please"
print(a)

m = "This is text"
m = 23
print(m)

unit_name = "Programming"
print(unit_name)
print("The 1st character is: ", unit_name[0])
print("The 4th character is: ", unit_name[3])
print("The 9th character is: ", unit_name[8])


greeting_string = "Welcome to Programming unit! This is a Level 4 unit :)"
print(greeting_string)
print("The first character is: ", greeting_string[0])
print("The fifth character is: ", greeting_string[4])
print(greeting_string[0:5])
print(greeting_string[-1])
print(greeting_string[-4:])

#greeting_string[0] = "X"
#print(greeting_string)

a=11
print(type(a)) # worked example
a = 11.0
print(type(a)) # print the type of a
a = "11"
print(type(a)) # print the type of a
a = "11" + "11"
print(type(a)) # print the type of a
a = "a"
print(type(a)) # print the type of a
a = True
print(type(a)) # print the type of a
a = "False"
print(type(a)) # print the type of a


x = "five"
y = 10
z = 20.2

print(type(x))
print(type(y))
print(type(z))
result_y_and_z = y + z
result_y_and_intz = y + int(z)
result_z_and_floaty = z + float(y)
result_concate_all = x + str(y) + str(z)
print(f"y + z = {result_y_and_z} and its data type is ", type(result_y_and_z))
print(f"y + int(z) = {result_y_and_intz} and its data type is ", type(result_y_and_intz))
print(f"z + float(y)) = {result_z_and_floaty} and its data type is ", type(result_z_and_floaty))
print(type(str(z)))
print(f"x + str(y) + str(z) = {result_concate_all} and its data type is ", type(result_concate_all))

'''
my-var = 1  # - is arithmetic operator
my_var$ = 1  # $ is illegal character
my_var_$ = 1  # $ is illegal character
2my_var = 1  # 2 is a digit, cannot start a name with anything other than text
my_var = 1  # this is ok
'''
