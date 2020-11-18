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
        self.blocked_damage = 0
        for armor in self.armor:
            self.blocked_damage -= armor.block()
        return self.blocked_damage

    def take_damage(self, damage):
        if abs(self.blocked_damage) < damage:
            rec_damage = damage + self.blocked_damage
            self.current_health -= rec_damage
            print(f"This is damage received: {rec_damage}")
        elif abs(self.blocked_damage) >= damage:
            rec_damage = 0
        return self.current_health



    def is_alive(self):
        if self.current_health > 0:
            return True
        elif self.current_health <= 0:
            return False

    def fight(self, opponent):
        fighters = [self, opponent]
        if not self.abilities or not opponent.abilities:
            print("Evenly Matched!")
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                pass




if __name__ == "__main__":
    hero1 = Hero("Voss", 200)
    hero2 = Hero("Fiji", 120)

    ability1 = Ability("Tummy Punch", 30)
    ability2 = Ability("Spank Cheeks", 90)
    ability3 = Ability("Booty Slap", 20)
    ability4 = Ability("Butt to Butt", 200)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    
    print(hero1.attack())

    armor = Armor("Chainmail", 100)
    another_armor = Armor("Paper Helmet", 20)
    hero1.add_armor(armor)
    hero1.add_armor(another_armor)
    print(hero1.defend())

    print(hero1.take_damage(210))

    print(hero1.is_alive())

    hero1.fight(hero2)