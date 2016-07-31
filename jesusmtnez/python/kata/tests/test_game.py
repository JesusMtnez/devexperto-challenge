import unittest
from game import Game

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def tearDown(self):
        self.g = None

    def _roll_many(self, n, pins):
        "Roll 'n' times a roll of 'pins' pins"
        for i in range(n):
            self.g.roll(pins)

    def _roll_spare(self):
        "Roll a spare"
        self.g.roll(5)
        self.g.roll(5)

    def _roll_strike(self):
        "Roll a strike"
        self.g.roll(10)

    def test_gutter_game(self):
        self._roll_many(20, 0)
        self.assertEqual(0, self.g.score())

    def test_all_ones(self):
        self._roll_many(20, 1)
        self.assertEqual(20, self.g.score())

    def test_one_spare(self):
        self._roll_spare()
        self.g.roll(3)
        self._roll_many(17, 0)
        self.assertEqual(16, self.g.score())

    def test_one_strike(self):
        self._roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self._roll_many(16, 0)
        self.assertEqual(24, self.g.score())

if __name__ == '__main__':
    unittest.main()
