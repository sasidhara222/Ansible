# BreakUp = open("E://Python Programming//BreakUp.txt",'r')
#
# for line in BreakUp:
#     if "naa" in line.lower():
#         print(line, end='')
#
# BreakUp.close()



# with open("E://Python Programming//BreakUp.txt",'r') as BreakUpSong:
#     for line in BreakUpSong:
#         if "naa" in line.lower():
#             print(line, end='')

# with open("E://Python Programming//BreakUp.txt",'r') as arjunReddy:
#     line = arjunReddy.readline()
#     while line:
#         print(line,end='')
#         line = arjunReddy.readline()


# with open("E://Python Programming//BreakUp.txt",'r') as arjunReddy:
#     line = arjunReddy.readlines()
# print(line)
#
# for lines in line[::-1]:
#     print(lines, end='')

# with open("E://Python Programming//BreakUp.txt",'r') as arjunReddy:
#     line = arjunReddy.read()
#
# for lines in line[::-1]:
#     print(lines, end='')

# Friuts = ["Grapes", "Orange", "Banana", "Pineapple", "Puchakai"]
#
# with open("E://Python Programming//Friuts.txt", 'w') as fruits_file:
#     for friut in Friuts:
#         print(friut, file=fruits_file)
#         print(friut, end='')

# Pandllu = []
#
# with open("E://Python Programming//Friuts.txt") as pandla_file:
#     for pandu in pandla_file:
#         Pandllu.append(pandu.strip('\n'))
#
# print(Pandllu)
#
# for pandu in Pandllu:
#     print(pandu)

# Movie_Details = "Kushi", "PawanKalyan", "Bhoomika", \
#                 ((1,"Ye mera Jaha"), \
#                 (2,"Ammaye Sanaga"), \
#                 (3,"Cheliya Cheliya"), \
#                 (4,"Premante Sulluvu Kadura"), \
#                 (5,"Holi Holia"), \
#                 (6,"Aduvarimatallaku"))
#
# Title, Actor, Actress, Songs = Movie_Details
#
# with open("E://Python Programming//Kushi.txt", 'w') as Kushi_File:
#     for detail in Movie_Details:
#         if type(detail) is tuple:
#             for tps in detail:
#                 print(tps)
#                 trakNo, trk = tps
#                 print(f"TrackNo.{trakNo} , Track: {trk}", file=Kushi_File)
#         else:
#             print(detail, file=Kushi_File)
# print(Movie_Details)
# print(tup2)

# cinema = ()
# with open("E://Python Programming//Kushi.txt", 'r') as kushiFile:
#     for det in kushiFile:
#         contents = det
#         print(contents)
with open("E://Python Programming//Tables.txt", 'w') as Yekallu:
    for i in range (1,11):
        for j in range (1,11):
            print("{} * {} = {}".format(i,j,i*j) , file=Yekallu)
        print('-' * 12, file=Yekallu)



# tup1 =  ("aaa","bbb",(1,"ccc"))
#
# for tups in tup1:
#     if type(tups) is tuple:
#         print(tups)



































