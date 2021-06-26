class ATM:
        def __init__(self,name,amount,pin):
            self.name=name
            self.amount=amount
            self.pin=int(pin)



suvan=ATM("Suvan",50000,234)
anup=ATM("Anup",500000,456)



while(True):
    a=input("enter your name")
    if a==suvan.name or a==anup.name:
        print("welcome to atm")
        break
    else:
        print("please try again")
    continue







while (True):
                b = int(input("enter your pin"))
                if a==suvan.name and b==suvan.pin:
                    break
                elif a==anup.name and b==anup.pin:
                    print("your balance is",anup.amount)
                    break
                else:
                    print("your pin is invalid.please try again")
                continue

inq = int(input("for balance inquiry press 1"))
if inq==1 and b==anup.pin:
        print("your balance is",anup.amount)
elif inq==1 and b==suvan.pin:
        print("your balance is",suvan.amount)





while(True):

            c = int(input("enter the amount you want to withdraw"))
            if a==suvan.name and b==suvan.pin and c<suvan.amount:
                    print("you have withdrawed",c,"amount")
                    d=suvan.amount-c
                    print("your remaining amount is",d)
                    break
            elif a==anup.name and  b==anup.pin and c<anup.amount:
                    print("you have withdrawed",c,"amount")
                    d=anup.amount-c
                    print("your remaining amount is",d)
                    break
            else:
                print("you dont have sufficient amount in your account.Please give a valid amount")
                continue







