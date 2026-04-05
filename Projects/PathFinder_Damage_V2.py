import random

def roll_to_hit():
    return random.randint(1,20)+29

def damage_dice():
    return random.randint(1, 12)

def normal_damage():
    total_normal_damage = 0
    for normal in range(3):
        roll3 = damage_dice()
        print(f"roll {normal+1}: {roll3}")
        total_normal_damage += roll3
    return total_normal_damage


def main():
  attack_roll = roll_to_hit()

  answer = input(f"You rolled {attack_roll}. Did you hit? Yes or No \n").lower()
  rage = input("Are you Raging? Yes or No\n")

  if answer == "yes":
      damage = normal_damage()+9
      print(f"Hit! You dealt {damage} damage!")
  else:
      print("Missed")

if __name__ == "__main__":
    main()