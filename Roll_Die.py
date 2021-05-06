import random

min=1
max=6

roll_die="Yes"

while (roll_die=="Yes"):
    print(random.randint(min,max))
    
    roll_die=input("Would you like to roll the die? [Yes/No]")
