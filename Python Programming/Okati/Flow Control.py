name = input("enter your name:")
age = int(input("how old are you {} ?".format(name)))

if age <= 18:
    print("come back after {} years".format(18 - age))
else:
    print("you have right to fucking vote, please go ahead and elect your fucking leader")


val = int(input("enter a numerical value:"))

if val > 0:
    print("you entered a positive value")
    if val < 100:
        print("your value is less than 100")
    else:
        print("your value is greater than 100")
elif val < 0:
    print("you entered a negitive value")
    if val > -100:
        print("your value is greater than -100")
    else:
        print("your value is less than -100")
else:
    print("your value is not valid, fuckoff!")

print(not True)
print(not False)

age = int(input("How old are you buddy?"))

if 15 <= age <= 65:
    print("Ogiee kelsa madi maganya")
else:
    print("Enjoy madi!")