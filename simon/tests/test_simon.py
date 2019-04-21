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
    
    def test_breaks(self):
        self.assertEqual(simon.breaks(3), "\n\n\n")
        self.assertEqual(simon.breaks(0), "")
    
    def test_game_header(self):
        self.assertEqual(simon.level_message([1,2,3], 1), "\033[1;95mSequence 1:\n\n\033[4m1 2 3")
    
    def test_validate_answer(self):
        self.assertEqual(simon.validate_answers('1234'), (None, True))
        self.assertEqual(simon.validate_answers('123a'), (3,False))
        self.assertEqual(simon.validate_answers('a23a'), (0, False))
        self.assertEqual(simon.validate_answers('15349'), (1, False))
        self.assertEqual(simon.validate_answers('12 349'), (2,False))
        self.assertEqual(simon.validate_answers('13""49'), (2,False))
        self.assertEqual(simon.validate_answers('4321'), (None, True))
    
    def test_check_answers(self):
        self.assertEqual(simon.is_correct([1,2,3], [1,3,4]), False)
        self.assertEqual(simon.is_correct([1,2,3], [1,2,3]), True)
        self.assertEqual(simon.is_correct([1,2], [1,2,3]), False)


if __name__ == "__main__":
    unittest.main()