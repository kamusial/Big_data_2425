import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from src.example import Warrior, Mage


class TestCharacterMovement(unittest.TestCase):
    def setUp(self):
        """Set up two characters, a warrior and a mage"""
        self.warrior = Warrior(name="Conan")
        self.mage = Mage(name="Merlin")

    def test_warrior_move_north(self):
        """Test warrior moving north"""
        self.warrior.move("N")
        self.assertEqual(
            self.warrior.current_pos, (2, 0)
        )  # Warrior moves 2 units north

    def test_warrior_move_east(self):
        """Test warrior moving east"""
        self.warrior.move("E")
        self.assertEqual(self.warrior.current_pos, (0, 2))  # Warrior moves 2 units east

    def test_mage_move_north(self):
        """Test mage moving north"""
        self.mage.move("N")
        self.assertEqual(self.mage.current_pos, (3, 0))  # Mage moves 3 units north

    def test_mage_move_east(self):
        """Test mage moving east"""
        self.mage.move("E")
        self.assertEqual(self.mage.current_pos, (0, 3))  # Mage moves 3 units east

    def test_warrior_shout(self):
        """Test warrior's shout"""
        self.assertEqual(self.warrior.shout(), "Roar!")

    def test_mage_cast_spell(self):
        """Test mage's spell casting"""
        self.assertEqual(self.mage.cast_spell(), "Abracadabra!")


if __name__ == "__main__":
    unittest.main()
