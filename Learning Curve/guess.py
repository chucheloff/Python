import random

number = int(input("player's number:\n"))
ace_count =0
count = 0
while count != 1:
    count = 0
    while not (random.randrange(number)+1) == number:
        count += 1
    print("computer randomly guessed you in %d guesses" % count)
    ace_count += 1
print("and also it also aced guessed you on the %d try" % ace_count)
