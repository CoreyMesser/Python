from os import sys
import random
from TT_Dungeon.character import Character
from TT_Dungeon.combat import Combat
from TT_Dungeon.monster import Dragon, Goblin, Troll


class Game(object):
    def setup(self):
        self.player = Character()
        self.monsters = [Goblin(), Troll(), Dragon()]

        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.inititive():
            print('** {} attacks! **'.format(self.monster))
            atk_dmg = self.monster.attack()
            if input('Will you try to dodge the {}\'s attack? [Y/N]'.format(self.monster)).lower == 'y':
                if self.player.dodge():
                    print('You dodged the attack!')
                else:
                    print('** You failed your dodge! **')
                    self.player.hp -= atk_dmg
            else:
                atk_dmg = self.monster.attack()
                print('{} hit you for {} of damage'.format(self.monster, atk_dmg))
                self.player.hp -= atk_dmg
        else:
            print('{} circles and doesn\'t attack'.format(self.monster))


    def player_turn(self):
        if self.player.inititive():
            player_choice = input('What would you like to do? ([A]ttack, [R]est, [Q]uit)').lower()
            if player_choice == 'a':
                print('** {} attacks! **'.format(self.player))
                if self.monster.dodge():
                    print('{} dodged your attack!'.format(self.monster))
                else:
                    atk_dmg = self.player.attack()
                    print('You hit {} for {} of damage'.format(self.monster, atk_dmg))
                    self.monster.hp -= atk_dmg
            elif player_choice == 'r':
                self.player.rest()
            elif player_choice == 'q':
                sys.exit()
        else:
            print('You do not attack')

    def cleanup(self):
        if self.monster.hp <= 0:
            self.player.leveled_up()
            self.monster = self.get_next_monster()
            # if self.get_next_monster() is None:
            #     print('You have vanquished the terrible monsters {}!'.format(self.player))
            #     if input('Would you like to play again? [Y/N]?').lower() == 'y':
            #         g = Game()
            #         g.__init__()
            #     else:
            #         sys.exit()
        if self.player.hp <= 0:
            print('You have been killed by the terrible monsters {}!'.format(self.player))
            if input('Would you like to play again? [Y/N]?').lower() == 'y':
                g = Game()
                g.__init__()
            else:
                sys.exit()


    def __init__(self):
        self.setup()

        while self.player.hp and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('\n'+'/'*20)
            self.player_turn()
            print('\n'+'/'*20)
            self.cleanup()
            print('\n'+'='*20)


        if self.player.hp:
            print('You win!')
        elif self.monsters or self.monster:
            print('You lose!')

if __name__ == '__main__':
    g = Game()
    g.__init__()
