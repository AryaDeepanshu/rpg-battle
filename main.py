from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Items

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


player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item":potion, "quantity": 5}, {"item":hipotion, "quantity": 5},
                {"item":superpotion, "quantity": 5}, {"item":elixer, "quantity": 5},
                {"item":highelixer, "quantity": 5}, {"item":grenade, "quantity": 5}]
player = Person(460, 65, 60, 34, player_magic, player_items)
enemy = Person(1200, 65, 45, 25, [],[])

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!" + bcolors.ENDC)

while running:
    print("===========================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    print("You chose ",choice)

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked enemy for", dmg, "points of damage. Enemy HP: ", enemy.get_hp())
    if index == 1:
        player.choose_magic()
        choice = int(input("Select Spell: ")) - 1
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
            enemy.take_damage(magic_dmg)
            print("You attacked enemy for", magic_dmg, "points of damage. Enemy HP: ", enemy.get_hp())
        print("You chose " + spell.name + " spell costing ", spell.cost, "mp")
    if index == 2:
        player.choose_item()
        item_chose = int(input("Choose Item: ")) - 1
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
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(item.name," fully restores HP/MP")
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print("You attacked enemy with ", item.name, " for ", item.prop, " HP")

    
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked you for", enemy_dmg, "points of damage. Your HP: ", player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.OKGREEN + "You lost!" + bcolors.ENDC)
        running = False
    print("================================")
    print("Enemy HP: ", enemy.get_hp(),"/",enemy.get_maxhp())
    print("Your HP: ", player.get_hp(),"/",player.get_maxhp())
    print("Your MP: ", player.get_mp(),"/",player.get_maxmp())