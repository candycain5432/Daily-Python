import random

die = int(input("""Which dice do you want to roll? (Enter the number on the left)
(1) 6 sides
(2) 10 sides
(3) 20 sides
(4) 50 sides
(5) 100 sides\n"""))

roll = None


if die == 1:
    roll = random.randint(1,6)
elif die == 2:
    roll = random.randint(1,10)
elif die == 3:
    roll = random.randint(1,20)
elif die == 4:
    roll = random.randint(1,50)
elif die == 5:
    roll = random.randint(1,100)

print(roll)
