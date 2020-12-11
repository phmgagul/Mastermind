import unittest
from io import StringIO
from unittest.mock import patch
import sys
from test_base import captured_io
from test_base import run_unittests
import mastermind


def is_between(code):

    #[0, 5, 9, 2]

    count = 0
    for i in range(len(code)):
        if code[i] in range(1, 9):
            count += 1

    if count == 4:
        return True
    else:
        return False

class MyTestCase(unittest.TestCase):

    def test_create_code(self):
        i = 0
        while i < 100:
            self.assertEqual(len(mastermind.create_code()), 4)
            self.assertEqual(is_between(mastermind.create_code()), True)
            i += 1

    def test_check_correctness(self):
        self.assertEqual(mastermind.check_correctness(2, False, 3), False)
        self.assertEqual(mastermind.check_correctness(1, False, 4), True)

    @patch("sys.stdin", StringIO("45214\n78412\n41234\n1234\n"))
    def test_get_user_input(self):
        self.assertEqual(mastermind.get_user_input(),"1234")

    @patch("sys.stdin", StringIO("1478\n"))
    def test_take_turn(self):
        self.assertEqual(mastermind.take_turn([1,4,7,8]),(4, 0))

    @patch("sys.stdin", StringIO("0576\n"))
    def test_take_turn_wrong_result(self):
        self.assertNotEqual(mastermind.take_turn([1,4,7,8]),(4, 0))