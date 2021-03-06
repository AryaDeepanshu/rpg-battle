import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items,type):
        self.maxhp = hp 
        self.name = name   
        self.hp = hp                  
        self.maxmp = mp    
        self.mp = mp    
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.type = type
        self.action = ["Attack", "Magic", "Items"]


    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)


    def update_dmg(self,list):
        type = list[0].type
        for i in list:
            if i.get_hp() == 0:
                list.remove(i)
                print(i.name, " defeated")
        if(len(list) < 1):
            if(type == "e"):
                print("You Won")
            else:
                print("Enemy Won")
            return False
        return list


    def take_damage(self,dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0
        return self.hp


    def get_hp(self):
        return self.hp


    def get_maxhp(self):
        return self.maxhp


    def get_mp(self):
        return self.mp


    def get_maxmp(self):
        return self.maxmp


    def reduce_mp(self,cost):
        self.mp -= cost


    def heal(self,dmg):
        if self.hp + dmg > self.maxhp:
            self.hp = self.maxhp
        else:
            self.hp += dmg


    def choose_enemy_spell(self):
        magic_choice = random.randrange(0,len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = self.generate_damage()
        pct = (self.hp/self.maxhp)*100
        if self.mp < spell.cost or spell.type == "White" and pct > 50:
            self.choose_enemy_spell()
        return spell, magic_dmg


    def choose_action(self):
        print("\n    "+self.name+"'s turn")
        print("    Actions: ")
        i = 1
        for item in self.action:
            print("        " + str(i)+ ".", item)
            i += 1


    def choose_magic(self):
        print("    Magics: ")
        i = 1
        for spell in self.magic:
            print("        " + str(i)+ ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1


    def choose_item(self):
        print("    Items: ")
        i = 1
        for item in self.items:
            print("        " + str(i)+ ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"])+")")
            i += 1

    def choose_target(self,enemies):
        print("    Enimes: ")
        i=1
        for enemy in enemies:
            print("        " + str(i)+ ".", enemy.name)
            i += 1
        choice = int(input("Choose Enemy: ")) -1
        return choice


    def get_enemy_stat(self):
        hp_bar = "???"*int((self.hp/self.maxhp)*100 / 2) + " "*(50-len(str("???"*int((self.hp/self.maxhp)*100 / 2))))
        hp_string = " "*(11-len(str(self.hp) + "/" + str(self.maxhp))) + str(self.hp) + "/" + str(self.maxhp)

        print("                               "+ 50*"_")
        print(self.name+":"+ (16-len(self.name))*" ", hp_string, "|" + hp_bar + "|")


    def get_stat(self):
        hp_bar = "???"*int((self.hp/self.maxhp)*100 / 4) + " "*(25-len(str("???"*int((self.hp/self.maxhp)*100 / 4))))
        mp_bar = "???"*int((self.mp/self.maxmp)*100 / 10) + " "*(10-len(str("???"*int((self.mp/self.maxmp)*100 / 10))))


        hp_string = " "*(11-len(str(self.hp) + "/" + str(self.maxhp))) + str(self.hp) + "/" + str(self.maxhp)
        mp_string = " "*(9-len(str(self.mp) + "/" + str(self.maxmp))) + str(self.mp) + "/" + str(self.maxmp)

        print("                               _________________________                  __________")
        print(self.name+":"+ (16-len(self.name))*" ", hp_string, "|" + hp_bar + "|     ", mp_string, "|" + mp_bar + "|")