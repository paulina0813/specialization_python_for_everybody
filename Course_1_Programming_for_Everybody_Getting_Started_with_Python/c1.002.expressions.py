#Using different exressions to see how they work

hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

#PEMDAS
x = 1 + 2 ** 3 / 4 * 5
print(x)

# Integer divisions
print(10 /2)
print(9 /2)
print(99 / 100)
print(10.0 / 2.0)
print(9.0 / 2.0)

# String conversions
sval = '123'
print(type(sval))
print(sval)

ival = int(sval)
print(type(ival))
print(ival + 1)

tval = str(ival)
print(type(tval))
print(tval)

# User Input
'''
We can instruct Python to pause and read data from the user usig the input() function
The input() function returns a string
'''

nam  = input('Who are you?')
print('Welcome', nam)
