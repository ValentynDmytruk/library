import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user import Reader

class TestUser(unittest.TestCase):

    def setUp(self):
        self.reader = Reader(1, "Валентин", "valentin@nuwm.edu.ua")

    def test_initial_state(self):
        self.assertEqual(self.reader.user_id, 1)
        self.assertEqual(self.reader.name, "Валентин")
        self.assertEqual(self.reader.email, "valentin@nuwm.edu.ua")

    @patch('builtins.print')
    def test_update_notifies_reader(self, mock_print):
        self.reader.update("Clean Architecture")
        expected_output = "[Reader UI] Валентин, гарна новина! У бібліотеці з'явилася книга: 'Clean Architecture'"
        mock_print.assert_called_once_with(expected_output)

if __name__ == '__main__':
    unittest.main()