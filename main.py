from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Items
import random


#Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 124, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

#White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

#Items
potion = Items("Potion", "potion", "Heals 50 HP", 50)
hipotion = Items("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Items("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Items("Elixer", "elixer", " Fully restores HP/MP of one party member", 99999)
highelixer = Items("Mega Elixer", "elixer", "Fully restores party's HP/MP", 99999)
grenade = Items("Grenade", "attack", "Deals 500 damage", 500)

#magic and item lists
player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item":potion, "quantity": 5}, {"item":hipotion, "quantity": 5},
                {"item":superpotion, "quantity": 5}, {"item":elixer, "quantity": 5},
                {"item":highelixer, "quantity": 5}, {"item":grenade, "quantity": 5}]

#players
player1 = Person("Clay:", 3260, 132, 60, 34, player_magic, player_items, "p")
player2 = Person("Hannah:", 4160, 188, 60, 34, player_magic, player_items, "p")
player3 = Person("Tony:", 3089, 174, 60, 34, player_magic, player_items, "p")

#enemies 
enemy1 = Person("Bryce:", 1200, 221, 70, 25, enemy_magic,[], "e")
enemy2 = Person("Monty:", 1200, 221, 65, 25, enemy_magic,[], "e")
enemy3 = Person("Jeff:", 1200, 221, 45, 25, enemy_magic,[], "e")

#player & enemy list
players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0
print("An Enemy Attacks!")

while running:
    print("================================")
    print("\n\n")
    print("NAME                          HP                                         MP")
    
    for player in players:
        player.get_stat()
    
    for enemy in enemies:
        enemy.get_enemy_stat()

    for player in players:
        
        player.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice) - 1
        print("\nYou chose ",player.action[index])

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked ", enemies[enemy].name, " for", dmg, "points of damage. Enemy HP: ", enemies[enemy].get_hp())
            update = enemies[enemy].update_dmg(enemies)
            
            if update != False:
                enemies = update
            else:
                running = False
                break
        
        if index == 1:
            player.choose_magic()
            choice = int(input("    Select Spell: ")) - 1
            
            if choice == -1:
                continue

            spell = player.magic[choice]
            
            if spell.cost > player.get_mp():
                print(bcolors.FAIL + "\n Not enough MP\n" + bcolors.ENDC)
                continue
            
            player.reduce_mp(spell.cost)
            magic_dmg = spell.generate_spell_damage()

            if spell.type == "White":
                player.heal(magic_dmg)
                print("You were healed by ", spell.name, "by ", spell.dmg," of HP.")
            else:
                dmg = player.generate_damage()
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print("You attacked", enemies[enemy].name,  "for", magic_dmg, "points of damage. Enemy HP: ", enemies[enemy].get_hp())
                update = enemies[enemy].update_dmg(enemies)
                
                if update != False:
                    enemies = update
                else:
                    running = False
                    break
            print("You chose " + spell.name + " spell costing ", spell.cost, "mp")
        
        if index == 2:
            player.choose_item()
            item_chose = int(input("    Choose Item: ")) - 1
            
            if item_chose == -1:
                continue
            
            item = player.items[item_chose]["item"]
            
            if player.items[item_chose]["quantity"] == 0:
                print("All ",player.items[item_chose]["item"].name, " are used.")
                continue
            player.items[item_chose]["quantity"] -= 1
            
            if item.type == "potion":
                player.heal(item.prop)
                print(item.name, " heals for: ", item.prop, " HP")
            elif item.type == "elixer":
                
                if item.name == "Mega Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(item.name," fully restores HP/MP")
            
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print("You attacked ", enemies[enemy].name, " with ", item.name, " for ", item.prop, " HP")
                update = enemies[enemy].update_dmg(enemies)
                
                if update != False:
                    enemies = update
                else:
                    running = False
                    break
    
    for enemy in enemies:
        enemy_choice = random.randrange(0,2)
        
        if enemy_choice == 0:
            target = random.randrange(0,len(players))
            enemy = enemies[random.randrange(0,len(enemies))]
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)

            print(enemy.name," attcked ",players[target].name, " for", enemy_dmg, " HP")
            update = players[target].update_dmg(players)
        
            if update != False:
                players = update
            else:
                running = False
                break
        
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            
            if spell.type == "heal":
                enemy.heal(magic_dmg)
                print(spell.name, " heals ", enemy.name, " for ", magic_dmg, " HP")
            elif spell.type == "Black":
                target = random.randrange(0,len(players))
                players[target].take_damage(magic_dmg)
                print(enemy.name, " attacks with ", spell.name, " with ", magic_dmg, " damage points")
                update = players[target].update_dmg(players)
                
                if update != False:
                    players = update
                else:
                    running = False
                    break