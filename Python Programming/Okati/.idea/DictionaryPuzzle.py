
locations = {
                0:"You are sitting infornt of Mi Daddy",
                1:"You are at Road",
                2:"You are at Hill Station",
                3:"You are in Building",
                4:"You are at River Valley",
                5:"You are in Forest"
}

exits = [
    {"Q":0},
    {"E":3, "W":2, "N":5, "S":4, "Q":0},
    {"N":5, "Q":0},
    {"W":1, "Q":0},
    {"W":2, "N":1, "Q":0},
    {"W":2, "S":1, "Q":0}
]

vocabulary = {
    "EAST": "E",
    "WEST": "W",
    "NORTH": "N",
    "SOUTH": "S",
    "QUIT": "Q"
}

loc = 1

while True:
    avaialbleExits = ""
    for direction in exits[loc].keys():
        avaialbleExits += direction + ","

    print(locations[loc])

    if loc == 0:
        break
    direction = input("Available exits are "+ avaialbleExits).upper()
    print()
    if len(direction)>1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
