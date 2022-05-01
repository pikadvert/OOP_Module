#import random
from models import Player
from models import Enemy
#from settings import *
from exceptions import *


class Game:
    def __init__(self):
        self.player = Player
        self.enemy = Enemy

    @staticmethod
    def play():
        """Start game WizardWarriorRobber"""
        while True:
            start = input("Please enter 'start' to start the game:").lower()
            if start != 'start':
                print("Invalid input, try again!")
            else:
                break
        player_name = input("Enter your name: ")
        player = Player(10, player_name)

        score = 0
        enemy_level = 1
        while True:
            enemy = Enemy(enemy_level)
            try:
                while True:
                    player.attack(enemy)
            except Enemydown:
                enemy_level += 1
                print('You won. New enemy_level: {}'.format(enemy_level))
                score += 5
            except GameOver:
                print('You lose. Your score: {}'.format(score))
                # Write score into file
                io_leaderboard = open("scores.txt", "r", encoding="utf-8")
                for line in io_leaderboard:
                    player_name, score = line.split()
                io_leaderboard.close()
                break
            finally:
                while True:
                    next_attempt = input('\nDo you wish to play again? (y/n): ').lower()
                    if next_attempt == 'n':
                        print("Good bye!")
                        exit()
                    elif next_attempt == 'y':
                        break
                    else:
                        print("Invalid input!\n")


if __name__ == "__main__":
    game = Game()
    game.play()

