class Character:
    current_pos = (0, 0)  # N/S, E/W

    def __init__(self, name):
        self.name = name

    def move(self, direction):
        ns, ew = self.current_pos
        if direction in ["N", "S"]:
            ns += self.speed
        else:
            ew += self.speed
        self.current_pos = (ns, ew)


class Warrior(Character):
    speed = 2

    def shout(self):
        return "Roar!"


class Mage(Character):
    speed = 3

    def cast_spell(self):
        return "Abracadabra!"


if __name__ == "__main__":
    player1 = Warrior("Conan")
    player2 = Mage("Houdini")

    player1.move("n")
    player2.move("s")

    print(player1.current_pos)
    print(player2.current_pos)
