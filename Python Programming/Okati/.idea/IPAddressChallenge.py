# ipAdd = input("Enter ip address:")
# octCount = 0
# numCount = 0
# for i in range (0,len(ipAdd)):
#     if ipAdd[i] == '.':
#         octCount += 1
#     elif ipAdd[i] != '':
#         numCount += 1
#     else:
#         print("Enter correct  ip address")
#
# print("Number of octanets in your IP: {}".format(octCount))
# print("Total number of values in your ip: {}".format(numCount))

ipAdd = input("Enter Ip Address:")
octCount = 1
numCount = 0

for char in ipAdd:
    if char != '.':
        numCount += 1
    else:
        print("No of values in {} octentant is: {}".format(octCount,numCount))
        numCount = 0
        octCount += 1

print("No of values in {} octentant is: {}".format(octCount,numCount))
print("Total number of octentants in your Ip is: {}".format(octCount))