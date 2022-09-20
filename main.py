import time
import random

# Defining important variables
playerstatus = 1
enemystatus = 1
playerhealth = 100
enemyAttacking = 0


# Function Definitions
def roll():
    global rollvar
    if input("type roll: ") == "roll":
        rollvar = random.randrange(2)
        print("you rolled a", rollvar + 1)


def randomroll(numroll):
    global playerchance
    playerchance = random.randrange(numroll)


def takedamage():
    global playerhealth
    global playerstatus
    playerhealth = playerhealth - 50
    if playerhealth <= 0:
        print(playername, "has died to", enemy)
        playerstatus = 0
    else:
        print(playername + "'s health is now", playerhealth)


def attackEnemy():
    global enemyHealth
    global enemystatus
    enemyHealth = enemyHealth - 50
    if enemyHealth <= 0:
        print(enemy, "has died to", playername)
        enemystatus = 0
    else:
        print(enemy + "'s health is now", enemyHealth)


def turn():
    inpaction = input("Choices:\ndodge:1\nblock:2\nattack:3\ntype 1, 2, or 3:")
    inpaction = int(inpaction)
    if inpaction == 1:
        if enemyAttacking != 0:
            randomroll(100)
            print("You've chosen to dodge")
            time.sleep(1)
            if playerchance < 35:
                if enemy == "snake":
                    print("The snake raises its head\n" + playername,
                          "tries to dodge but trips over himself and falls\nthe snake attacks successfully\n")
                    takedamage()
                    time.sleep(1)
                elif enemy == "scorpion":
                    print("The scorpion's tail sways\n", playername,
                          "tries to dodge but trips over himself and falls\nthe scorpion attacks successfully\n")
                    takedamage()
                    time.sleep(1)
            else:
                if enemy == "snake":
                    print("The snake raises it's head to strike\nJust as the snake comes down to strike", playername,
                          "leaps out of the way\n")
                    time.sleep(1)
                elif enemy == "scorpion":
                    print("The scorpion's tail sways\nJust as the scorpion's tail comes down to strike", playername,
                          "leaps out of the way\n")
                    time.sleep(1)
        else:
            print("The", enemy, "was not attacking. ", playername, "dodges nothing")
            time.sleep(1)
    elif inpaction == 2:
        print("You've chosen to block")
        time.sleep(1)
        if inpweapon == 1:
            print("The ", enemy, "attacks and you attempt to block with your sword\n",
                  playername + "'s blocking was ineffective")
            takedamage()
            time.sleep(1)
        else:
            print("The ", enemy, " attacks and you attempt to block with your hammer\n",
                  playername + "'s blocking was ineffective")
            takedamage()
            time.sleep(1)
    elif inpaction == 3:
        print("You've chosen to attack")
        if enemyAttacking != 0:
            print("The", enemy, "is much faster than", playername, "it strikes first.")
            takedamage()
            time.sleep(1)
        else:
            print("You choose to attack the enemy")
            randomroll(100)
            if playerchance > 25:
                attackEnemy()
                time.sleep(1)
            else:
                print(playername, "tries to strike the", enemy, "and misses.\n")
                time.sleep(1)

# Name the player
print("hello welcome to the game.")
time.sleep(.5)
playername: str = input("Name your character: ")

# Decide enemy
print("Welcome to the game", playername, "You will be fighting 1 of 2 monsters")
time.sleep(.5)
print("You will fight either a giant snake or a giant scorpion")
time.sleep(.5)
print("Roll the dice to decide your foe")
roll()

if rollvar != 0:
    enemy = "scorpion"
else:
    enemy = "snake"
print("you will be fighting a", enemy)
time.sleep(1)

# Decide Weapon
inpweapon = input("you have 2 weapon options:\nsword:1\nhammer:2\ntype 1 or 2: ")
inpweapon = int(inpweapon)

if inpweapon == 1:
    print("you chose a sword")
elif inpweapon == 2:
    print("you chose a hammer")
time.sleep(1)

# Announce encounter
if enemy == "snake":
    print(
        "As soon as you pick up your weapon, a giant snake slithers through a long hallway\nIt rears its head, "
        "ready to strike")
    enemyHealth = 100
elif enemy == "scorpion":
    print(
        "As soon as you pick up your weapon, a giant scorpion skitters through a massive doorway\nIt positions its "
        "tail high in the air, ready to strike")
    enemyHealth = 100
time.sleep(1)

# Run first turn (enemy attacking)
enemyAttacking = 1
print("This battle will be legendary")
time.sleep(.75)
turn()

# Run second turn (player attacking)
enemyAttacking = 0
print("the", enemy, "rests for a moment\nIt is your turn.")
turn()

# Run infinite turns until death
while enemystatus + playerstatus == 2:
    if enemyAttacking == 0:
        enemyAttacking = 1
        if enemy == "snake":
            print("The snake rears its head, ready to strike")
        else:
            print("The scorpion positions its tail high in the air, ready to strike")
        turn()
    else:
        enemyAttacking = 0
        print("the", enemy, "rests for a moment\nIt is your turn.")
        turn()
else:
    print("game over")
