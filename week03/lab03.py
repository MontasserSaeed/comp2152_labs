import random
# Dice Options created using list() and range()
diceOptions = list(range(1, 7))

# Weapons list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

print("Available Weapons: ", ', '.join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
        else:
             print("Invalid Input! Please enter a number between 1-6")

combatStrength = getCombatStrength("Please enter a number between 1-6 for Player: ")
mCombatStrength = getCombatStrength("Please enter a number between 1-6 for Monster: ")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    print(f"\n Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"\n Hero selected {heroWeapon}, Monster selected {monsterWeapon}")
    print(f" Hero Total Strength: {heroTotal}, Monster Total Strength: {monsterTotal}")

    if heroTotal > monsterTotal:
        print("Hero Wins!")
    elif heroTotal < monsterTotal:
        print("Monster Wins!")            
    else:
        print("It's a tie!")            