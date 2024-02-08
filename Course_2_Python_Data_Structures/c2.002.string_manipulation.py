'''
STRING CONCATENATION
- When the '+' operator is applied to strings, it's called "concatenation"
'''
a = 'Hello'
b = a + 'There'
print(b)

#Consider spaces
c = a + ' ' + 'There'
print(c)

'''
USING in AS A LOGICAL OPERATOR
- The in keyword can also be used to check to see if one string is "in" another string
- The in expression is a logical expression that returns True or False and can be used in an if statement
'''
fruit = 'banana'
'n' in fruit     #True
'm' in fruit     #False
'nan' in fruit   #True
if 'a' in fruit:
    print('Found it')

'''
STRING COMPARISON
- For strings, a is considered the lowest and z is considered the highest
- Upper case letters are considered bigger than lowe case letters
- Numbers are considered lower than lowe case letters
'''    
word = input("Enter a word: ")

if word == 'banana':
    print('All right, bananas.')
if word < 'banana':
    print("Your word " + word + ', comes before banana.')
elif word > 'baanana':
    print("Your word " + word + ", comes after banana.")
else:
    print("All right, bananas")

'''
STRING LIBRARY
- Python has a number of string functions which are in teh string library
- These functions are already built into every string - we invoke them by appending the function to the string variable
- These functions do not modify the original string, instead they return a new string that has been altered
- .lower() is a methhod
'''
greet = 'Hello Bob'
zap = greet.lower() #Makes all the letters lower case
print(zap)          #Prints the modified string where all the letters are loweer case
print(greet)        #Prints the original string with upper case letters

print('Hi There'.lower())

'''
SEE THE NETHODS IN THE CLASS
'''
stuff = 'Hello world'
type(stuff)
dir(stuff)   #Shows us the methods in the class stuff

'''
SEARCHING A STRING
- Similar to in but instead of just returning True or False if it finds it, it tells you where it found it
- We use the find() function to search for a substring within another string
- find() finds the first occurrence of the substring
- If the substring is not found, find() returns -1
- Remember that string position starts at 0
'''
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

'''
SEARCH AND REPLACE
- The replace() function is like a "search and replace" operation in a word processor
- It replaces all occurrences of the search string with the replcement string
'''
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')  #Replaces the part of the string that says 'Bob' with Jane
print(nstr)                          #Prints 'Hello Jane'

nstr = greet.replace('o', 'X')       #Replaces all the 'o' in the string with 'X'
print(nstr)                          #Prints 'HellX BXb'

'''
STRIPPING WHITESPACE
- Sometimes we want to take a string and remove whitespace at the beginning and/or end
- lstrip() and rstrip() remove whitespace at the left or right
- strip() removes both beginning and ending whitespace
'''
greet = ' Hello Bob   '
greet.lstrip()
greet.rstrip()
greet.strip()

'''
PREFIXES
'''
line = 'Please have a nice day'
line.startswith('Please')
line.startswith('P')

'''
PARSING AND EXTRACTING
'''
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)    #Prints the position where it finds the '@'

sppos = data.find(' ', atpos)
print(sppos)     #Prints the position where it finds the first space after the starting value (in this case it's atpos). The second parameter tells Python where to start looking

host = data[atpos + 1 : sppos] #It tells Python to print everything after the '@' (atpos + 1) up until (not including)  the space position(sppos).
print(host)