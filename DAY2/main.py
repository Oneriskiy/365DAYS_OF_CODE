class Hero:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


    def info(self):
        return f" Hero haves {self.health} HP and {self.damage} Damage"


    def attack(self, other):
        count = 0
        while True:
            if count % 2 == 0:
                other.health -= self.damage
                print(f"{other} hp: {other.health}\n")
                count += 1
                if other.health <= 0:
                    print(f"Противник {other} Побежден!")
                    break
            else:
                self.health -= other.damage
                print(f"{self} hp: {self.health}\n")
                count += 1
                if self.health <= 0:
                    print(f"Наш персонаж: {self} Побежден!")
                    break


class Doctor(Hero):
    def __init__(self, health, damage, regeneration):
        super().__init__(health, damage)
        self.regeneration = regeneration


    def regeneration_hp(self):
        if self.health <= 105:
            self.health += self.regeneration
        else:
            print("you already have a lot of health")
    def __str__(self):
        return "Доктор"

    def info(self):
        text = super().info()
        return f"{text} and {self.regeneration} Regeneration"

class Prince(Hero):
    def __init__(self, health, damage, shield):
        super().__init__(health, damage)
        self.shield = shield


    def defense(self, incoming_damage):
        if self.shield > 0:
            self.shield -= incoming_damage
            if self.shield < 0:
                self.health += self.shield
                self.shield = 0
    def __str__(self):
        return "Принц"

def menu():
    menu_asc = int(
        input(
            """Выберите нужное действие:
        1 - Играть за Мага против Принца    
        2 - Играть за Принца Против Мага             
        >>
                    """.strip()))
    if menu_asc == 1:
        prince = Prince(130, 40, 40)
        doctor = Doctor(115, 20, 15)
        doctor.attack(prince)
    if menu_asc == 2:
        prince = Prince(130, 40, 40)
        doctor = Doctor(115, 20, 15)
        prince.attack(doctor)

if __name__ == "__main__":
    menu()

