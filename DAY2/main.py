class Hero:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


    def info(self):
        return f" Hero haves {self.health} HP and {self.damage} Damage"


class Doctor(Hero):
    def __init__(self, health, damage, regeneration):
        super().__init__(health, damage)
        self.regeneration = regeneration


    def regeneration_hp(self):
        if self.health <= 105:
            self.health += self.regeneration
        else:
            print("you already have a lot of health")


    def info(self):
        text = super().info()
        return f"{text} and {self.regeneration} Regeneration"

class Prince(Hero):
    def __init__(self, health, damage, shield):
        super().__init__(health, damage)
        self.shield = 40


    def defense(self, incoming_damage):
        if self.shield > 0:
            self.shield -= incoming_damage
            if self.shield < 0:
                self.health += self.shield
                self.shield = 0


if __name__ == "__main__":
    my_doctor = Doctor(115, 10, 5)
    print(my_doctor.info())
