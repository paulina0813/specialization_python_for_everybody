# Counting in a loop
# To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop
zork = 0
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)

# Summing in a loop
# To add up a value we encounter on a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop
zork = 0
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)

# Finding the average in a loop
# An average just combines he counting and sum patterns and divides when the loop is gone
count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)

# Filtering in a loop
# We use an if statement in the loop to catch / filter the values we are looking for
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("Large Number", value)
print("After")

# Search using a Boolean variable
# If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After")

'''
THE "IS" AND "IS NOT" operators
- Python has an 'is" operator that can be used in logical expressions
- Implies "is the same as"
- Similar to, but stronger than ==
- "is not" is also a logical operator
'''

# Finding the smallest value
smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)