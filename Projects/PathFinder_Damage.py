import random

def attack_dice():
   attack = random.randint(1,20)
   return attack

def damage():
    damages = random.randint(1, 12)
    return damages

def normal_damage():
    total_normal_damage = 0
    for i in range(4):
        roll2 = damage()
        #print(f"roll {i+1}: {roll2}")
        total_normal_damage += roll2
    return total_normal_damage


def crit_damage():
    total_damage = 0
    for i2 in range(8):
        roll = damage()
        #print(f"roll {i2+1}: {roll}")
        total_damage += roll
    return total_damage


print(f"will you hit? {attack_dice()+21}")
damages = input("Yes or No: \n").lower()


if damages == "no":
    print("No Damage")
elif damages == "yes":
    crit = input("Did You Crit? Yes or No: \n").lower()

    if crit == "yes":
        print(f"Crit Damage Total: {crit_damage()+12}")
    else:
        print(f"Normal Damage Total: {normal_damage()+7}")