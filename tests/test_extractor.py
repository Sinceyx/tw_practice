import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from read_json_util import read_json_file
from src.extractor import extract


class TestCaseOfExtractor(unittest.TestCase):

    def test_extract_give_native_dict_should_return_specific_string(self):
        dic = {'name': 'Jack', 'age': 12}
        jq_path = '.name'
        expect_result = 'Jack'
        self.assertEqual(expect_result, extract(dic, jq_path))

    def test_extract_should_return_specific_string(self):
        dic = read_json_file('../resource/test_extract_should_return_specific_string.json')
        jq_path = '.path'
        expect_result = '/community/support.html'
        self.assertEqual(expect_result, extract(dic, jq_path))

    def test_extract_should_return_none(self):
        dic = read_json_file('../resource/test_extract_should_return_none.json')
        jq_path = '.anything'
        expect_result = None
        self.assertEqual(expect_result, extract(dic, jq_path))

    def test_extract_should_return_specific_json(self):
        dic = read_json_file('../resource/test_extract_should_return_specific_json.json')
        jq_path = '.result.data.markdownRemark.fields'
        expect_result = {
            "path": "content/community/support.md",
            "slug": "community/support.html"
        }
        self.assertEqual(expect_result, extract(dic, jq_path))
