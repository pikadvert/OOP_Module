import random
import numpy as np

from settings import *
from exceptions import Enemydown, GameOver



class Enemy:
    """Enemy model implementation"""

    def __init__(self, level) -> None:
        """Initialize model instance"""
        self.level = level
        self.lives = level
        self.allowed_choices = VALID_CHOICES

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise Enemydown("Enemy down", 1)

    @staticmethod
    def select_attack() -> int:
        """Return random fight choice"""
        return np.random.choice(VALID_CHOICES)

    @staticmethod
    def fight(func1, func2):
        result = 0
        if func1 == func2:
            result += 0
        elif func1 == WIZARD and func2 == WARRIOR:
            result += 1
        elif func1 == WARRIOR and func2 == ROBBER:
            result += 1
        elif func1 == ROBBER and func2 == WIZARD:
            result += 1
        elif func1 == WARRIOR and func2 == WIZARD:
            result -= 1
        elif func1 == WIZARD and func2 == ROBBER:
            result -= 1
        elif func1 == ROBBER and func2 == WARRIOR:
            result -= 1
        return result

class Player(Enemy):
    """Player model implementation"""
    def __init__(self, level, name: str) -> None:
        super(Player, self).__init__(level)
        self.name = name

    def __str__(self) -> str:
        return self.name

    def select_attack(self):
        """Return player`s fight choice"""
        choice = int(input("Enter your choice: 1 if WIZARD, 2 if WARRIOR, 3 if ROBBER: "))
        while choice not in self.allowed_choices:
            choice = int(input("Invalid choice. Please try again: "))
        return choice


    def attack(self, enemy_obj):
        defense = enemy_obj.select_attack()  # Random choise
        attack = self.select_attack()  # User input
        self.fight = Enemy.fight(attack, defense)
        print("Your attack: {}, enemy attack: {}".format(attack, defense))
        if self.fight == 0:
            print("It's a draw!")
        elif self.fight == 1:
            enemy_obj.decrease_lives()
            print("You attacked successfully!")
        elif self.fight == -1:
            self.lives -= 1
            if self.lives >= 0:
                raise GameOver("Game over", 1)
            print("You missed!")
