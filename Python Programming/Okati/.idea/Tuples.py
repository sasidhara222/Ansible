# t = "a","b", "c"
# print(t)
#
# x = ["a","b", "c"]
# print(x)
#
# print("a","b", "c")
# print(("a","b", "c"))
#
# Tholiprema = "Ninilla", "Ninilla", "Chusanyee..!", 2018 #Mutable object
# tholiprema = "Ni", "Manasyee", "syee", 1998
#
# print(Tholiprema)
# print(tholiprema)
#
# print(Tholiprema[1])
# # Tholiprema[2] = "Mi Daddy"
#
# Tholiprema = Tholiprema[0], "Mi Daddy", Tholiprema[2], "Pikinav Thi"
# print(Tholiprema)
#
# Tholiprema = ["Ninilla", "Ninilla", "Chusanyee..!", 2018] #immutable object
# print(Tholiprema[1])
# Tholiprema[2] = "Mi Daddy"
# print(Tholiprema)


MyAlbum = "Sasidhara", "Raaga", 2018, ([(1,"AAAA"), (2,"BBBB"), (3,"CCCC"), (4,"DDDD")])
MyAlbum[3].append((5,"EEEE"))
Title, Album, Year, Tracks = MyAlbum
Tracks.append((6,"FUCK"))
print(MyAlbum)
print(Title)
print(Album)
print(Year)
for song in Tracks:
    trkNo, tune = song
    print("\t Track No.{} Song:{}".format(trkNo,tune))



























