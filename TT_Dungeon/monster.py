import random
from TT_Dungeon.combat import Combat


COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):

    min_hp = 1
    max_hp = 1
    min_exp = 1
    max_exp = 1
    weapon = 'sword'
    sound = 'roar'
    base_atk = 1
    max_atk = 1
    # loot/armor etc

    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hp,
                                              self.exp)
        # self.hit_points = kwargs.get('hit_points', 1)
        # self.weapon = kwargs.get('weapon', 'sword')
        # self.color = kwargs.get('color', 'yellow')
        # self.sound = kwargs.get('sound', 'ROAR')

    def battlecry(self):
        return self.sound.upper()

    def attack(self):
        roll = random.randint(self.base_atk, self.max_atk)
        return roll

    def inititive(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4


class Goblin(Monster):
    max_hp = 3
    max_exp = 2
    sound = 'squeak'
    max_atk = 5


class Troll(Monster):
    min_hp = 3
    max_hp = 10
    max_exp = 10
    sound = "gurgle"
    base_atk = 2
    max_atk = 7


class Dragon(Monster):
    min_hp = 10
    max_hp = 20
    min_exp = 10
    max_exp = 20
    base_atk = 5
    max_atk = 10