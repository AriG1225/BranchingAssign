#Branching Assignment due June 19th
#If statment/branching zy 3.5 => 3.25.2
kwH = int(input("KW hours used:"))
print()

if (kwH <= 1000):
    totalBill = (kwH * 0.07633)
elif (kwH > 1000):
    totalBill = (76.33 + ((kwH - 1000) * 0.09259))
print("Your amount owed is:", totalBill)

