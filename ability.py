import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        attack_damage = random.randint(0, self.max_damage)
        return attack_damage

if __name__ == "__main__":
    ability = Ability("Thunderbolt", 20)
    
    print(ability.name)
    print(ability.attack())