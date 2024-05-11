'''
Try and except is usually used when you have a piece of code that might fail
It's a way to catch a traceback error
The try and except clause is a safety net
You want to try to minimize the amount of code that you put into the try and excepts o you can reduce the risk of lines not running and you can figure out what is 
blowing up the code
'''
# When the first conversion fails, it will just drop into the except clause and continue
astr  = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

# When the second conversion succeeds, it just skips the except clause and the program continues
astr = '1234'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

# Sample try / except
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a number')