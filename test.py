import unittest
from utilities import guess_number

class TestGen(unittest.TestCase):
    def test_guess_low(self):
        ans = guess_number(6, 8)
        self.assertEqual(ans, "Low")

    def test_guess_high(self):
        ans = guess_number(8, 3)
        self.assertEqual(ans, "High")

    def test_guess_right(self):
        ans = guess_number(4, 4)
        self.assertEqual(ans, "Right")
        
if __name__ == '__main__':
    unittest.main()