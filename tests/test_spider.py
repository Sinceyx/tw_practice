import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest import mock
from read_json_util import read_json_file
from spider import extract_house_address_infos, extract_address


class TestSpider(unittest.TestCase):

	@mock.patch("spider.AtrealtyWebSpider")
	def test_extract_house_address_infos(self, mock_atrealty_spider):
		fake_spider = mock_atrealty_spider.return_value
		fake_spider.data_array = read_json_file('../resource/test_spider.json')
		expected_result = [
							  {
							    "postal_code" : "2711-40013",
							    "permalink" : "https://www.atrealty.com.au/hay-nsw-2711-40013/",
							    "state_name" : "hay-nsw"
							  },
							  {
							    "postal_code" : "2447-40083",
							    "permalink" : "https://www.atrealty.com.au/15-kingfisher-lane-congarinni-north-nsw-2447-40083/",
							    "state_name" : "15-kingfisher-lane-congarinni-north-nsw"
							  },
							  {
							    "postal_code" : "2262-40076",
							    "permalink" : "https://www.atrealty.com.au/30-iluka-avenue-san-remo-nsw-2262-40076/",
							    "state_name" : "30-iluka-avenue-san-remo-nsw"
							  },
							  {
							    "postal_code" : "2448-40087",
							    "permalink" : "https://www.atrealty.com.au/3-9-ridge-street-nambucca-heads-nsw-2448-40087/",
							    "state_name" : "3-9-ridge-street-nambucca-heads-nsw"
							  },
							  {
							    "postal_code" : "2140-40015",
							    "permalink" : "https://www.atrealty.com.au/71-172-parramatta-road-homebush-nsw-2140-40015/",
							    "state_name" : "71-172-parramatta-road-homebush-nsw"
							  }
							]
		self.assertNotEqual(expected_result, extract_house_address_infos(fake_spider))  # add assertion here

	@mock.patch("spider.AtrealtyWebSpider")
	def test_extract_address(self, mock_atrealty_spider):
		fake_spider = mock_atrealty_spider.return_value
		fake_spider.data_array = read_json_file('../resource/test_spider.json')
		expected_result ={}
		self.assertNotEqual(expected_result, extract_address(fake_spider))  # add assertion here

