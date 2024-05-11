'''
Comparison Operators:
<  | Less than
<= | Less than or equal to
== | Equal to
>= | Greater than or equal to
>  | Greater than
!= | Not equal

- Boolean expressions ask a question and produce a Yes or No result whichbwe can use to control de flow
- Boolean expressions using comparison operators evaluate to True / False or Yes / No
- Comparison operators look at variables but do not change the variables
- Remember: '=' is used for assignment

'''


#Program
x=5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

## ONE WAY DECISIONS

#Example
x=5

if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or equal to 5')
if x <= 5:
    print('Less than or equal to 5')
if x != 6:
    print('Not equal to 6')

#Example 2
x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')

#Example 3
# Nested -  block within a block
x = 5
if x > 2:
    print('Bigger than 2')
    print("Still bigger than 2")
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All done')

## TWO WAY DECISIONS

#Example 4
x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')

## MULTI WAY DECISIONS

#Example 5
#x = 0
#x = 5
x = 13
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')

#Example 6
#x = 0
#x = 5
#x = 13
#x = 34
#x = 89
x = 1989
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else:
    print('Ginormous')