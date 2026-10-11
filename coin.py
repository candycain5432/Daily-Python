import random

list = ["Heads", "Tails"]

h = 0
t = 0

flipnum = int(input("How many flips do you want?\n"))

for i in range(flipnum):

    flip = random.choice(list)
    
    if flip == "Heads":
        h += 1
    elif flip == "Tails":
        t += 1





print(f"Heads:{h} Tails:{t}")
    

