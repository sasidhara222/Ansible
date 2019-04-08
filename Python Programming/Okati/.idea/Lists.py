Strings = ["str1","str2","str3","str4","str5"]
Strings.append("Midaddy")
for word in Strings:
    print("This is " + word)

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
#numbers.sort()
print(sorted(numbers))

##########################################33
even = [2,4,6,8]

another_even = list(even)

another_even.sort(reverse=True)

print(even)
###############################################
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for i in number_set:
        print(i)