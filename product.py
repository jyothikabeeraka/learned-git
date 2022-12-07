
product1 = int(input("product1 sold"))
product2 = int(input("product2 sold"))
if (product1<=0 or product2<=0):
    print("enter a positive number")
product3 = int(input("product3 sold"))
total = product1*40+product2*50+product3*60
print("totalPayment would be",total )
