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
		expected_state_names = ['hay-nsw', '15-kingfisher-lane-congarinni-north-nsw', '30-iluka-avenue-san-remo-nsw', '3-9-ridge-street-nambucca-heads-nsw', '71-172-parramatta-road-homebush-nsw']
		expected_postal_codes = ['2711-40013', '2447-40083', '2262-40076', '2448-40087', '2140-40015']
		expected_permalinks = ['https://www.atrealty.com.au/hay-nsw-2711-40013/', 'https://www.atrealty.com.au/15-kingfisher-lane-congarinni-north-nsw-2447-40083/', 'https://www.atrealty.com.au/30-iluka-avenue-san-remo-nsw-2262-40076/', 'https://www.atrealty.com.au/3-9-ridge-street-nambucca-heads-nsw-2448-40087/', 'https://www.atrealty.com.au/71-172-parramatta-road-homebush-nsw-2140-40015/']

		actual_result = extract_house_address_infos(fake_spider)

		actual_state_names = actual_result.get('state_names')
		actual_postal_codes = actual_result.get('postal_codes')
		actual_permalinks = actual_result.get('permalinks')

		self.assertTrue(str(expected_state_names)==str(actual_state_names) and str(expected_postal_codes)==str(actual_postal_codes) and str(expected_permalinks)==str(actual_permalinks))

	@mock.patch("spider.AtrealtyWebSpider")
	def test_extract_address(self, mock_atrealty_spider):
		fake_spider = mock_atrealty_spider.return_value
		fake_spider.data_array = read_json_file('../resource/test_spider.json')
		actual_result = extract_address(fake_spider)
		expected_result =['Hay, NSW, 2711', '15 Kingfisher Lane, Congarinni North, NSW, 2447', '30 Iluka Avenue, San Remo, NSW, 2262', '3/9 Ridge Street, Nambucca Heads, NSW, 2448', '71/172 Parramatta Road, Homebush, NSW, 2140']
		self.assertEqual(expected_result, actual_result)

