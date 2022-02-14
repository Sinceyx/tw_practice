import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.spider import crawl


class TestSpider(unittest.TestCase):

	def test_crawl(self):
		call_return = crawl()

		expected_type = list
		actual_return_type = type(call_return)
		self.assertTrue(expected_type, actual_return_type)

		expected_size = 5
		actual_size = len(call_return)
		self.assertEqual(expected_size, actual_size)





