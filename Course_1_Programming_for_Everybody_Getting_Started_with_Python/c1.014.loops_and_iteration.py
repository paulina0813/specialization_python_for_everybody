'''
REPEATED STEPS
- Loops (repeated steps) have iteration variables that change each time through a loop
- Often these iteration variables go through a sequence of numbers

WHILE LOOPS
- While loops run until one condition is false, and then it breaks
'''

# while loop 1
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)

'''
BREAK STATEMENT
To avoid getting trapped in a loop, there are some statements that we can use to break out of the loop
- Break statement
    + The break statement ends the current loop and jumps to the statement immediately following the loop
    + It is like a loop test that can happen anywhere in the body of the loop
'''

# while loop 2
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print("Done!")

'''
CONTINUE
- The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration
- Break skips out of the loop and continue skips back to the top of the loop
- Continue goes to the next iteration
'''
while True:
    line = input("> ")
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("Done!")