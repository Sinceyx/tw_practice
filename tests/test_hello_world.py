import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.hello_world import say_hi


class TestCaseOfHelloWorld(unittest.TestCase):
    def test_say_hi(self):
        name = "Xin.Yu"
        expected = "Hello " + name
        self.assertEqual(expected, say_hi(name))



