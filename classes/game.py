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
    def __init__(self, name, hp, mp, atk, df, magic, items):
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
        self.action = ["Attack", "Magic", "Items"]


    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)


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
        self.hp += dmg


    def choose_action(self):
        print("    "+self.name)
        print("    Actions: ")
        i = 1
        for item in self.action:
            print("        " + str(i)+ ".", item)
            i += 1


    def choose_magic(self):
        print("\n    Magics: ")
        i = 1
        for spell in self.magic:
            print("        " + str(i)+ ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1


    def choose_item(self):
        print("\n    Items: ")
        i = 1
        for item in self.items:
            print("        " + str(i)+ ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"])+")")
            i += 1


    def get_stat(self):
        hp_bar = ""
        hp_bar_ticks = (self.hp/self.maxhp)*100 / 4

        mp_bar = ""
        mp_bar_ticks = (self.mp/self.maxmp)*100 / 10
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = " "*(11-len(str(self.hp) + "/" + str(self.maxhp))) + str(self.hp) + "/" + str(self.maxhp)
        mp_string = " "*(9-len(str(self.mp) + "/" + str(self.maxmp))) + str(self.mp) + "/" + str(self.maxmp)

        print("                              _________________________                  __________")
        print(self.name + (16-len(self.name))*" ", hp_string, "|" + hp_bar + "|     ", mp_string, "|" + mp_bar + "|")