from mock import patch
import unittest
import simon

class TestSimon(unittest.TestCase):
    @patch('builtins.input', return_value='q')
    def test_get_choice(self, random_input):
        self.assertEqual(simon.continue_game(), False)

    @patch('builtins.input', return_value='a')
    def test_continue_game(self, random_input):
        self.assertEqual(simon.continue_game(), True)


if __name__ == "__main__":
    unittest.main()