#Write a program to accept 3 digit number . If the first digit is double pf second digit and half of third digit then display "Yes,ypu have done it",othervise display "Please try next time "


num = int(input('Enter a 3 digit number:'))

d1 = num % 10    
num = num // 10  

d2 = num % 10    
num = num // 10   

d3 = num % 10   
num = num // 10

if(d3 == 2 * d2 and d3 == d1 / 2):
    print('Yes, you have done it.')
else:
    print('Please try next time.')