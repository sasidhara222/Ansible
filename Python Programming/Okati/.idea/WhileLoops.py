# i = 0
# while i < 10:
#     i += 1
#     print("i is now: {}".format(i))

# import random
#
# Highest = 10
# guess = 0
# answer = random.randint(1,Highest)
# print("Your python has value between 1 and {}, Guees it.! :".format(Highest))
# while guess != answer:
#     guess  = int(input())
#     if guess == 0:
#         print("Thanks for your time..!")
#         break
#     elif guess < answer:
#         print("Enter HIgher:")
#     elif guess > answer:
#         print("Enter Lower:")
#     else:
#         print("Correct guess..!")


import random
count = 0
guess = 0
Start = 1
End = 100
Mid = int(End/2)
answer = random.randint(Start,End)

print("Python had value between 1 and {}, can you guess it.! :".format(End))
guess = int(input())
while guess != answer:
    if guess == 0:
        print("Thanks for your time.! Answer is.. {}".format(answer))
        break
    elif Start < answer < Mid:
        count += 1
        guess = input("Clue No.{}, Answer is b/w {} and {}:".format(count,Start,Mid))
        if guess == answer:
            print("You guessed it at No.{} try..! The answer is.. {} ".format(count+1,answer))
            break
        Start = Start + 1
        End = Mid
        Mid = int((Start+End)/2)
    elif Mid < answer < End:
        count += 1
        guess = input("Clue No.{}, Answer is b/w {} and {}:".format(count,Mid,End))
        if guess == answer:
            print("You guessed it at No.{} try..! The answer is.. {} ".format(count+1,answer))
            break
        Start = Mid + 1
        End = End
        Mid = int((Start+End) / 2)
    else:
        print("You guessed it at No.{} try..! The answer is.. {} ".format(count+1,answer))
        break