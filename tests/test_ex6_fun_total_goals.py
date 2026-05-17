import unittest
import pandas as pd

from src.exercises.ex6 import fun_total_goals


class TestFuntotalGoals(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data_local = [1, 2, 3]
        data_visitant = [4,5,6]
        data = pd.DataFrame({'FTHG':data_local, 'FTAG':data_visitant})
        result = fun_total_goals(data)
        self.assertEqual(result, (6,15,21))


if __name__ == '__main__':
    unittest.main()