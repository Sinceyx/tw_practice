import unittest
import json
from extractor import extract


def read_json_file(file_path):
    text = ''
    with open(file_path, "r") as f:
        text += f.read()
    dic = json.loads(text)
    return dic


class TestCaseOfExtractor(unittest.TestCase):

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
