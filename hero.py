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
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armor.append(armor)

    def defend(self):
        blocked_damage = 0
        for armor in self.armor:
            blocked_damage -= armor.block()
        return blocked_damage

    def take_damage(self, damage):
        self.damage = damage

    def is_alive(self):
        pass

    def fight(self, opponent):
        fighters = [self.name, opponent.name]
        winner = random.choice(fighters)
        return f"{winner} won!"


if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)

    ability = Ability("Tummy Rub", 50)
    another_ability = Ability("Spank Cheeks", 90)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

    armor = Armor("Chainmail", 100)
    another_armor = Armor("Paper Helmet", 20)
    hero.add_armor(armor)
    hero.add_armor(another_armor)
    print(hero.defend())