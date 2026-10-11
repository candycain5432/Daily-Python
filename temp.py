"""
got tired of this program because for the life of me i couldnt remember how to use global variables
anyway this is scalable tecnicaly 
10/8/2026
Temperture converter
"""


# questions to select units can add Temperture

n = int(input("""Select your starting unit: (type the number on the left)
(1) Fahrenheit
(2) Celsius
"""))

x = int(input("""Select desierd unit: 
(1) Fahrenheit
(2) Celsius
"""))

# Global variables
rtemp = 0


# The math 

def FtoC():
    global rtemp
    temp = int(input("Enter temperture in Fahrenheit"))

    # Math

    rtemp += ((temp - 32) * 5/9)
    print(rtemp)


def CtoF():
    global rtemp
    temp = int(input("Enter temperture in Celsius"))

    # Math

    rtemp += ((temp * 9/5) + 32)
    print(rtemp)


# This if statment uses the two inputs at the top to find the correct function to use

if n == 1 and x == 2:
    FtoC()
elif n == 2 and x == 1:
    CtoF()
