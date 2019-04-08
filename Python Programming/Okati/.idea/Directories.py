Heros = {"Cheranjeevi":"popularly known as Mega Star",
         "Venkatesh":"Popularly known as Victory",
         "Pawan Kalyan":"Popularly known as Power star",
         "Mahesh babu":"popularly known as super star"
         }

# print(Heros)


# print(Heros["Cheranjeevi"])
# print(Heros["Pawan Kalyan"])

# while True:
#     HeroInput = input("Enter Heros name: \n")
#     if HeroInput == "quit":
#         break
#     elif HeroInput in Heros:
#         print(Heros[HeroInput])
#     else:
#         print("Your {} is not in list".format(HeroInput))

Orderedmanner = list(Heros.keys())
Orderedmanner.sort()
print(Orderedmanner)

for i in Orderedmanner:
    print(i + " - " + Heros[i])
