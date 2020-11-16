import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.ability = ability

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


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        pass

















if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero("Batman")
    hero2 = Hero("Superman")

    print(hero1.fight(hero2))