import random
class player:
  def __init__(self, health, attack):
    self.health = health
    self.attack = attack
    
  def stats(self):
    print("\nSTATS")
    print("Health:", self.health)
    print("Attack:", self.attack)
class Enemy:
  def __init__(self):
    enemy_name = ["Dragon", "Ogre", "Werewolf", "Troll", "Stone Warrior", "Centuar"]
    enemy_attack = [20, 10, 15, 5, 25, 30]
    enemy_health = [40, 30, 20, 50, 10, 25]
    self.health = enemy_health[random.randint(0,5)]
    self.attack = enemy_attack[random.randint(0,5)]
    self.name = enemy_name[random.randint(0,5)]
  def stats(self):
    print("\nEnemy STATS")
    print("Species:", self.name)
    print("Health:", self.health)
    print("Attack:", self.attack)
dude = player(100, 20)
def game_loop():
  defeat_enemy_counter = 0
  
  print("You have accidently wandered into a magical forest and have nothing but a wand that shoots lasers. Can you survive?")
  while(dude.health > 0 and defeat_enemy_counter < 6):
    direction = input("\nYou see 3 paths that you can take \n[Forward], [Right], or [Left] ")
    if(direction == "left" or direction == "Left" or direction == "l" or direction == "L" or direction == "r" or direction == "R" or direction == "right" or direction == "Right" or direction == "forward" or direction == "Forward" or direction == "f" or direction == "F"):
      Continue = True
      badguy = Enemy()
      print("\nYou've encountered...")
      badguy.stats()
      while(badguy.health > 0 and Continue == True):
        choice = input("\nWould you like to [Attack] or [Run] ")
        if(choice == "Attack" or choice == "attack" or choice == "a" or choice == "A"):
          dude.health -= badguy.attack
          badguy.health -= dude.attack
          print("\nThe",badguy.name,"attacks you doing",badguy.attack,"damage to you\n""Then you attack the "+badguy.name+", and do",dude.attack,"damage to the",badguy.name)
          dude.stats()
          badguy.stats()
        elif(choice == "Run" or choice == "run" or choice == "r" or choice == "R"):
          dude.health -= 20
          badguy.health -= badguy.health
          Continue = False
          print("\nYou chose to run away from the enemy but the enemy hurts you while you escape")
          dude.stats()
        else:
          print("\nPlease enter a valid choice\n20 health points shall be taken from you because you have not entered a invalid choice")
          dude.health -= 20
          dude.stats()
        if(dude.health <= 0):
          break
      if (badguy.health <= 0):
        defeat_enemy_counter += 1
      elif(dude.health <= 0):
        print("\nYou lose!\n")
      elif(defeat_enemy_counter == 6):
        print("\nYou have succesfully escaped the magical forest!")
    else:
      print("\nPlease enter a valid choice\n20 health points shall be taken from you because you have not entered a invalid choice")
      dude.health -= 20
      dude.stats()
      if(dude.health <= 0):
        print("\nYou lose!")
game_loop()