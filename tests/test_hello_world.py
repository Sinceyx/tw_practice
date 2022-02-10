"""
    unit_test for app.say_hi function
"""

import unittest
from hello_world import say_hi


class AppTestCase(unittest.TestCase):
    def test_say_hi(self):
        """
            function test of say_hi
        """
        name = "Xin.Yu"
        expected = "Hello " + name
        self.assertEqual(expected, say_hi(name))  # add assertion here



