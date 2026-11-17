#write a program to given 3 digit number is palindrome or not.

num = int(input('Enter a 3 digit number:'))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

if d1 == d3:
    print('The number is a palindrome.')
else:
    print('The number is not a palindrome.')