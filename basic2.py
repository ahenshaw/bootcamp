#### flow control ####

#-----------------------------------------
# iterating
for i in range(10):
    print(i, end=" ")
print()

#-----------------------------------------
for value in (2,3,"orange"):
    print(value)

#-----------------------------------------
# conditional
a = 0
if a == 0:
    print('a is 0')

#-----------------------------------------
# multi-level conditional
a = 3
if a == 0:
    print('a is 0')
elif a < 0:
    print('a is negative')
else:
    print('a is positive')

#-----------------------------------------
# looping
a = 0
while True:
    a += 1
    if a >= 10:
        break
print('a is', a)
