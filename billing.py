sum = 0
while(True):
    bill = input("Enter the item price and press e to exit:\n")
    if(bill!='e'):
        sum = sum + int(bill)
        print(f"YOUR TOTAL BILL IS : {sum}")
        
    else:
        print(f"YOUR TOTAL BILL IS : {sum}")
        break
print("Thanks for shopping with us!!!")