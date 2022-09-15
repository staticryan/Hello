import time
import random

import public as public


playerstatus = 1
enemystatus = 1
playerhealth = 100
enemyAttacking = 0

def roll():
    global rollvar
    if input("type roll: ") == "roll":
        rollvar = random.randrange(2)
        print("you rolled a ", rollvar + 1)

def turn():
    inpaction = input("Choices:\ndodge:1\nblock:2\nattack:3\ntype 1, 2, or 3:")
    inpaction = int(inpaction)
    if inpaction == 1:
        if enemyAttacking != 0:
            playerchance = random.randrange(2)
            print("You've chosen to dodge")
            if playerchance != 1:
                if enemy == "snake":
                    print("The snake raises its head\n", playername,
                          "tries to dodge but trips over himself and falls\n the snake attacks successfully")
                    takedamage()
                elif enemy == "scorpion":
                    print("The scorpion's tail sways\n", playername,
                          "tries to dodge but trips over himself and falls\n the scorpion attacks successfully")
                    takedamage()
            else:
                if enemy == "snake":
                    print("The snake raises it's head to strike\n Just as the snake comes down to strike ", playername,
                          " leaps out of the way\n")
                elif enemy == "scorpion":
                    print("The scorpion's tail sways\n Just as the scorpion's tail comes down to strike ", playername,
                          " leaps out of the way\n")
        else:
            print("The", enemy, "was not attacking. ", playername, "dodges nothing")
    elif inpaction == 2:
        print("You've chosen to block")
        if inpweapon == 1:
            print("The ", enemy, " attacks and you attempt to block with your sword\n",
                  playername + "'s blocking was ineffective")
            takedamage()
        else:
            print("The ", enemy, " attacks and you attempt to block with your hammer\n",
                  playername + "'s blocking was ineffective")
            takedamage()
    elif inpaction == 3:
        print("You've chosen to attack")
        if enemyAttacking != 0:
            print("The enemy is much faster than", playername, "it strikes first.")
            takedamage()
        else:
            print("You attack the enemy")


def takedamage():
    global playerhealth
    global playerstatus
    playerhealth = playerhealth - 50
    if playerhealth <= 0:
        print(playername, "has died to ", enemy)
        playerstatus = 0
    else:
        print(playername + "'s health is now ", playerhealth)




print("hello welcome to the game.")
playername: str = input("Name your character: ")

print("Welcome to the game", playername, "You will be fighting 1 of 2 monsters")
print("You will fight either a giant snake or a giant scorpion")
print("Roll the dice to decide your foe")
roll()

if rollvar != 0:
    enemy = "scorpion"
else:
    enemy = "snake"
print("you will be fighting a ", enemy)

inpweapon = input("you have 2 weapon options:\nsword:1\nhammer:2\ntype 1 or 2: ")
inpweapon = int(inpweapon)

if inpweapon == 1:
    print("you chose a sword")
elif inpweapon == 2:
    print("you chose a hammer")

if enemy == "snake":
    print(
        "As soon as you pick up your weapon, a giant snake slithers through a long hallway\nIt rears its head, ready to strike")
    enemyHealth = 100
elif enemy == "scorpion":
    print(
        "As soon as you pick up your weapon, a giant scorpion skitters through a massive doorway\n It positions its tail high in the air, ready to strike")
    enemyHealth = 150

enemyAttacking = 1
print("This battle will be legendary")
turn()

while enemystatus + playerstatus == 2:
    print("the snake rests for a moment\n It is your turn.")
    enemyAttacking = 0
    turn()
    if enemyAttacking == 0:
        enemyAttacking = 1
else:
    print("game over")
