from classes.game import Person,bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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
    else:
        player.choose_magic()
        choice = input("Select Spell: ")
        index = int(choice) - 1
        cost = player.get_spell_mp_cost(index)
        if cost > player.get_mp():
            print(bcolors.FAIL + "\n Not enough MP\n" + bcolors.ENDC)
            continue
        player.reduce_mp(cost)
        print("You chose " + player.get_spell_name(index) + " spell costing ", player.get_spell_mp_cost(index), "mp")

        magic_dmg = player.generate_spell_damage(index)
        enemy.take_damage(magic_dmg)
        print("You attacked enemy for", magic_dmg, "points of damage. Enemy HP: ", enemy.get_hp())

    
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
    print("Your MP: ", player.get_mp(),"/",player.get_maxmp()``