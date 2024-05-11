'''
1. Looking inside strings
- We can get any single character in a string using an indez specified in square brackets
- The index value must be an integer and it starts at zero
- The index value can be an exprssion that is computed
'''
fruit = "banana"
letter = fruit[1]
print(letter)

x = 3
w = fruit[x-1]
print(w)

'''
2. A character too far
- You will get a python error if you attempt to index beyond the end of a string
- Be careful when indexing values and slices
'''
zot = 'abc'
#print(zot[5]) #This will produce an error because there is no indez 5 in that string

'''
3. Strings have length
-  The built-in function len gives us the length of a string
- A function is some stored code that we use. A function takes some input and produces an output
'''
fruit = 'banana'
print(len(fruit))

'''
4. Lopping through Strings
- Using a while statement and an iteration variable, and the len function, we can construct a loop to look at each of the letters in a string individually
- A definite loop using a for statement is much more elegant
- The iteration variable is completely taken care of by the for loop
'''
#while loop - indefinite loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#for loop - definite loop
fruit = 'banana'
for letter in fruit:
    print(letter)
    
'''
5. Looping and Counting
- There is a simple loop that loops through each letter in a string and counts the number of times the loop encounters the 'a' character
'''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

'''
6. Looking Deeper into in
- The iteration variables "iterates" through the sequence (ordered set)
- The block (body) of code is executed once for each value in the sequence
- The iteration variable moves through all of the values in the sequence
'''
for letter in 'banana':
    print(letter)

'''
7. Slicing strings
- We can also look at any continuous section of a string using a colon operator
- The second number is one beyond the end of the slice - "up to but not including"
- If the second number is one beyond the end of the string, it stops at the end
'''
s = 'Monty Python'
print(s[0:4]) #prints 'Mont'
print(s[6:7]) #prints 'P'
print(s[6:20]) #prints 'Python


#If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively
s = 'Monty Python'
print(s[:2]) #prints 'Mo'
print(s[8:]) #prints 'thon'
print(s[:]) #prints 'Monty Python'