import random

def main():
    rage = input("Are you in Raged? Yes or No \n").lower()
    if rage == "no":
        attack_damage_dice(is_raging=False)
    elif rage == "yes":
        attack_damage_dice(is_raging=True)
    else:
        print("Invalid input.")

def attack_damage_dice(is_raging):

    def attack_dice():
       attack = random.randint(1,20)
       return attack

    def damage():
        damages = random.randint(1, 12)
        return damages

    def normal_damage():
        total_normal_damage = 0
        for normal in range(4):
            roll2 = damage()
            print(f"roll {normal+1}: {roll2}")
            total_normal_damage += roll2
        return total_normal_damage

    def crit_damage():
        total_damage = 0
        for crit2 in range(8):
            roll = damage()
            print(f"roll {crit2+1}: {roll}")
            total_damage += roll
        return total_damage


    print(f"will you hit? {attack_dice()+28}")
    damages = input("Yes or No: \n").lower()


    if damages == "no":
        print("No Damage")
    elif damages == "yes":
        crit = input("Did You Crit? Yes or No: \n").lower()

        base_bonus = 9
        crit_bonus = 9

        if is_raging:
            base_bonus += 6
            crit_bonus += 6


        if crit == "yes":
            print(f"Crit Damage Total: {crit_damage()+ crit_bonus}")
        else:
            print(f"Normal Damage Total: {normal_damage() + base_bonus}")
    else:
        print("Invalid input. Please enter Yes or No.")


main()