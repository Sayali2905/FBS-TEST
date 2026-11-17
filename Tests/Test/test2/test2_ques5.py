#A man goes to a shop and buys 5 products. Write a program to accept the price of each product and display the total bill after adding 18% GST.

p1 = int(input('Enter price of product 1:' ))
p2 = int(input('Enter price of product 2:' ))
p3 = int(input('Enter price of product 3:' ))
p4 = int(input('Enter price of product 4:' ))
p5 = int(input('Enter price of product 5:' ))

total_price = p1 + p2 + p3 + p4 + p5
GST = total_price * 0.18
total_bill = total_price + GST

print(f'Total bill after adding 18% GST is: {total_bill}')
