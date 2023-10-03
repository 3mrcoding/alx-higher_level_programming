#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lD = abs(number) % 10

if number > 0:
    if lD > 5:
        print(f"Last digit of {number} is {lD} and is greater than 5")
    elif lD < 6 and lD != 0:
        print(f"Last digit of {number} is {lD} and is less than 6 and not 0")
    elif lD == 0:
        print(f"Last digit of {number} is {lD} and is 0")
else:
    if lD == 0:
        print(f"Last digit of {number} is {lD} and is 0")
    else:
        print(f"Last digit of {number} is {-lD} and is less than 6 and not 0")
