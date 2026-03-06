class Hero:
    """
    Parent class, initializes the character's health and damage.
    Attributes:
    health (int): Character's health
    damage (int): Character's damage
    Methods:
    info(): Returns character information
    attack(): Stores combat logic
    """

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def info(self):
        return f" The hero has {self.health} HP and {self.damage} damage"

    def attack(self, other):
        count = 0
        while True:
            if count % 2 == 0:
                other.health -= self.damage
                print(f"{other} hp: {other.health}\n")
                count += 1
                if other.health <= 0:
                    print(f"The enemy {other} is defeated!")
                    break
            else:
                self.health -= other.damage
                print(f"{self} hp: {self.health}\n")
                count += 1
                if self.health <= 0:
                    print(f"Our character {self}  is defeated!")
                    break


class Doctor(Hero):
    """
        A class derived from the Hero, incorporating the Doctor's abilities: regeneration.
    Attributes:
    regeneration (int): Character regeneration
    Methods:
    regeneration_hp(): Character regeneration logic
    info(): Returns character information
    constructor __str__(): Returns the character type
    """

    def __init__(self, health, damage, regeneration):
        super().__init__(health, damage)
        self.regeneration = regeneration

    def regeneration_hp(self):
        if self.health <= 105:
            self.health += self.regeneration
        else:
            print("you already have a lot of health")

    def __str__(self):
        return "Doctor"

    def info(self):
        text = super().info()
        return f"{text} and {self.regeneration} Regeneration"


class Prince(Hero):
    """
    A class derived from the Hero, incorporating the Prince's abilities: shield.
    Attributes:
    defense (int): Character's shield
    Methods:
    defense(): Character defense logic
    info(): Returns character information
    constructor __str__(): Returns character type
    """

    def __init__(self, health, damage, shield):
        super().__init__(health, damage)
        self.shield = shield

    def defense(self, incoming_damage):
        if self.shield > 0:
            self.shield -= incoming_damage
            if self.shield < 0:
                self.health += self.shield
                self.shield = 0

    def info(self):
        text = super().info()
        return f"{text} and {self.shield} shield"

    def __str__(self):
        return "Prince"


def initializing_characters():
    prince = Prince(130, 40, 40)
    doctor = Doctor(115, 20, 15)
    return prince, doctor


def menu():
    initializing_characters()
    prince, doctor = initializing_characters()
    menu_asc = int(
        input(
            """          
        Select the desired action:
        1 - Play as the Mage against the Prince
        2 - Play as the Prince against the Mage
        3 - Display information about a character
        >>
                """.strip()
        )
    )
    if menu_asc == 1:
        doctor.attack(prince)
    if menu_asc == 2:
        prince.attack(doctor)
    if menu_asc == 3:
        hero_choice = int(
            input(
                """
        Choose a character from the list below:
        1 - Doctor
        2 - Prince
        """.strip()
            )
        )
        if hero_choice == 1:
            print(doctor.info())
        elif hero_choice == 2:
            print(prince.info())


if __name__ == "__main__":
    menu()
