'''
ARGUMENTS
- An argument is a value we pass into the function as its input when we call the function
- We use arguments so we can direct the function to do different kinds of work when we call it at different times
- We put the arguments in parentheses after the name of the function

PARAMETER
- A parameter is a variable which we use in the function definition
- It is a "handle" that allows the code in the funtion to access the arguments for a particular function invocation
'''
#Function 1
#lang is an argument
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
        
#parameter 'es'
greet('es')
#paramenter 'fr'
greet('fr')
#parameter 'en'
greet('en')

'''
RETURN VALUES
- Often a function will take its arguments, do some computation, nd return a variable to be used as the value of the function callin the calling expression. The 
return keyword is used for this
- A "fruitful" function is one that produces a result (or return value).
- A return statements ends the function execution and "sends back" the result of the function
- The return value is used to communicat the result of the function t the real world

RETURN STATEMENT
1. Stops the function
2. Determines the residual value
'''

#Function 2
def greet():
    return "Hello"

print(greet(), "Glenn")
print(greet(), "Sally")

#Function 3 Return Values
def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(greet("en"), "Glenn")
print(greet("fr"), "Sally")
print(greet("es"), "Michael")

'''
MULTIPLE PARAMETERS / ARGUMENTS
- We can define more tha one parameter in the function definition
- We simply add more arguments when we call the function
- We match the number and order of arguments and parameters
'''
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)