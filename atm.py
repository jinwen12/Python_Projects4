money=float(input("How much money you want to get?"))
balance=float(5000)
difference=balance-money
if difference>0 or difference==0:
    print("Here is your money:$",format(money,'.2f'),". Your balance is:$",format(difference,'.2f'))
elif difference<0:
    print("Sorry you do not have enough balance.")
print("Thank you!")
