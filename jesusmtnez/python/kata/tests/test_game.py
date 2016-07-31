import unittest
from game import Game

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def tearDown(self):
        self.g = None

    def test_gutter_game(self):
        for i in range(20):
            self.g.roll(0);

        self.assertEqual(0, self.g.score())

    def test_all_ones(self):
        for i in range(20):
            self.g.roll(1)

        self.assertEqual(20, self.g.score())

if __name__ == '__main__':
    unittest.main()
