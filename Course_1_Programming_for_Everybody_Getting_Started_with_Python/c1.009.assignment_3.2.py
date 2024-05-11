''' 
Rewrite your assignment 1 pay computation using try and except so that your program handles non numeric input gracefully by printing a message and exiting the
program
'''

sh = input('Enter hours: ')
sr = input('Enter rate: ')

try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error, please enter a numeric input')
    quit()
    
print(fh, fr)

if fh <= 40:
    print('Regular Pay')
    gross_pay = fh * fr
else:
    print('Overtime')
    reg = 40 * fr
    otp = (fh - 40) * fr * 1.5
    gross_pay = reg + otp
print('Pay:', gross_pay)