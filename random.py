import random

diceRoll = input('How many rolls? ')
diceSides = input('How many sides of the die? ')
#2&3 asking for number of rolls and sides

diceRoll = int(diceRoll)
diceSides = int(diceSides)
#1 dice rolls and sides are intigers

for i in range(diceRoll):
    randomDice = random.randrange(diceSides)+1
#4 rolling dice ^
    print (randomDice)
#5 dice output
    if randomDice==20 and diceSides==20:
        print('critical hit')
    if randomDice==1 and diceSides==20:
        print('critical fail')
#6&7 checking for crit miss and fails

print ('done rolling')

# https://www.w3schools.com/python/python_conditions.asp
# https://github.com/zeyang77/Pythontest2
