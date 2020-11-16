from ability import Ability
from armor import Armor
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armor = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        pass

    def defend(self, incoming_damage):
        self.incoming_damage = incoming_damage

    def take_damage(self, damage):
        self.damage = damage

    def is_alive(self):
        pass

    def fight(self, opponent):
        fighters = [self.name, opponent.name]
        winner = random.choice(fighters)
        return f"{winner} won!"


if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)