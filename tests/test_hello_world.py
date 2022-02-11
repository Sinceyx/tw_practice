"""
    unit_test for app.say_hi function
"""
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.hello_world import say_hi


class TestCaseOfHelloWorld(unittest.TestCase):
    def test_say_hi(self):
        """
            function test of say_hi
        """
        name = "Xin.Yu"
        expected = "Hello " + name
        self.assertEqual(expected, say_hi(name))  # add assertion here



