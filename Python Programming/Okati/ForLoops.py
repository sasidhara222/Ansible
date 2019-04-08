for i in range(1,18):
    print("i is now {}".format(i))

number = "1,22,333,4444,55555"
for i in range(0,len(number)):
    if number[i] in "123456789":
        print(number[i],end='')

number = "1,25,369,36589,159357"
cleanNumber = ""
for char in number:
    if char in "0123456789":
        cleanNumber += char
print(int(cleanNumber))

for i in range (0,100,5):
    print("{}".format(i))

for i in range(1,11):
    for j in range(1,11):
        print("{}*{}={}".format(i,j,i*j),end='\t')
    print('')

marketList = ["Biyam", "Pappullu", "Godumapindi", "IdlyRava"]
for item in marketList:
    print(item + " Konalye")

plateBojanam = ["Annam", "Pappu", "Sambar", "cabbage", "Rasam", "Perugu", "Kakarakaya"]
unLikeFood = ''

for item in plateBojanam:
    if item == 'cabbage':
        print("Naku cabbage vaddu")
        continue
    elif item == 'Kakarakaya':
        print("Kakarakaya thisesi Ice Cream pettu")
        break
    print(item +' '+"Bagundi!")

