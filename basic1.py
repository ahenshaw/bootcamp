print("Hello, World! Here's some basic Python.")

#### some built-in datatypes ####
#-----------------------------------------
# create an integer and give it a name
a = 3
print("a is", a)

#-----------------------------------------
# create a floating-point number and give it a name
b = 2.2
print("b is", b)

#-----------------------------------------
# do some math on integer and floating point
print("a * b is", a * b)

#-----------------------------------------
# using f-string interpolation
print(f"{a} * {b} is {a * b}")

#-----------------------------------------
# create a string and give it a name
string = "This is a string"
print("string is", string)

#-----------------------------------------
# change the objects referred to by a, b, & string
a = 4.1; b = 2; string="new string"

#-----------------------------------------
# create a list and give it a name
l = [1, 2, a*b, string]
print("l is", l)
print("len(l) is", len(l))
print("l[0] is", l[0])

#-----------------------------------------
# change the last value in the list
l[-1] = "changed"
print("l is", l)

#-----------------------------------------
# create a dict (dictionary/map/hash) and give it a name
d = {"red": 0xff0000, "green": 0x00ff00, "blue": 0x0000ff}
print("d is", d)
print("d['blue'] is", d["blue"])

#-----------------------------------------
# create a set and give it a name
s = {1,1,2,3,5,"fibonacci"}
print("s is", s)


