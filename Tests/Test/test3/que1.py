#WAP to print first n prime numbers

n = int(input("Enter how many prime numbers: "))

num = 2
count = 0

while count < n:
    if num > 1:
        i = 2
        while i < num:
            if num % i == 0:
                break
            i = i + 1

        if i == num:
            print(num, end=" ")
            count = count + 1

    num = num + 1