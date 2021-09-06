#Pooja would like to withdraw X $US from an ATM.
#The cash machine will only accept the transaction if X is a multiple of 5,
#Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges).
#For each successful withdrawal the bank charges 0.50 $US.
#Calculate Pooja's account balance after an attempted transaction.



wd=int(input("enter withdrawal amount:"))
acc=int(input("account balance:"))
if((0<wd<=2000)and(0<=acc<=2000)):
    if((acc>=(wd+0.5))and(wd%5==0)):
     bal=acc-(wd+0.5)
     format_float = "{:.2f}".format(acc)
     print(format_float)   
    
    else:
        format_float = "{:.2f}".format(acc)
        print(format_float)
else:
     format_float = "{:.2f}".format(acc)
     print(format_float)
