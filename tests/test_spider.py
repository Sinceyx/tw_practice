import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import spider as sp


class TestSpider(unittest.TestCase):

	def test_capture_house_infos_from_atrealty(self):
		self.assertEqual(True, False)  # add assertion here

	def test_extract_address(self):
		sp.extract_address()


	def test_extract_address(self):
		sp.extract_address()