import random
from TT_Dungeon.combat import Combat
from TT_Dungeon.monster import Monster


class Character(Combat):
    attack_limit = 10
    exp = 0
    base_hp = 1
    max_hp = 10
    dodge = 5
    level = 1

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        if self.weapon == 'axe':
            roll += 2
        return roll

    def get_weapon(self):
        weapon_choice = self.weapon = input('Weapon ([S]word, [A]xe, [B]ow):').lower()
        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif weapon_choice == 'a':
                return 'axe'
            elif weapon_choice == 'b':
                return 'bow'

    def __init__(self, **kwargs):
        self.monster = Monster()
        self.name = input("Name: ")
        self.weapon = self.get_weapon()
        self.hp = random.randint(self.base_hp, self.max_hp)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{}, HP: {}, XP: {}'.format(self.name, self.hp, self.exp)

    def rest(self):
        if self.hp < self.base_hp:
            self.hp += 1

    def leveled_up(self):
        self.exp += self.monster.exp
        if self.exp == '5':
            self.level += 1
        elif self.exp == '10':
            if self.level != 2:
                self.level +=2
            self.level += 1
        elif self.exp == '15':
            self.level += 1
        print('Level {}! You\'ve leveled up!! Power courses through you'.format(self.level))
