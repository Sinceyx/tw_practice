"""
    A program to capture data from website: https://www.atrealty.com.au/
"""
import re
import jq
import json
import requests
from extractor import extract


def capture_product_infos_from_atrealty(nums: int):
    home_page_url = 'https://www.atrealty.com.au/buy/'
    first_response = requests.post(home_page_url)
    head = first_response.headers
    url = 'https://www.atrealty.com.au/wp-json/hi-api/v1/properties?page=1&per_page=' + str(nums) + '&listing=residential&price_type' \
                                                                                               '=sale&tags_field=&search-id=983&auction=&inspection=&location=&sub_type=any&min_price=&max_price=&min_bedrooms' \
                                                                                               '=&max_bedrooms=&min_bathrooms=&max_bathrooms=&parking=&surrounding_suburbs=1&suburb=&state=&latlng='
    result = json.loads(requests.get(url, head).text)
    return json.loads(jq.compile('.data').input(result).text())


data_array = capture_product_infos_from_atrealty(5)


def extract_address():
    address_array = []
    for item in data_array:
        address_array.append(extract(item, '.name'))
    return address_array


def extract_house_address_infos_from_permalink():
    house_info_array = []
    for item in data_array:
        permalink = extract(item, '.permalink')
        permalink_pattern = re.compile('/?[^./][0-9a-z-]*/?$')
        permalink_regex_search_result = permalink_pattern.search(permalink).group().replace('/', '')
        house_address_info = HouseAddressInformation(extract_state_name_from_permalink(permalink_regex_search_result),extract_postal_code_from_permalink(permalink_regex_search_result))
        house_info_array.append(house_address_info)
    return house_info_array


def extract_state_name_from_permalink(permalink: str):
    state_name_pattern = re.compile('^[1-9]?[0-9-]*[a-z-]*[a-z]')
    search_result = state_name_pattern.search(permalink).group()
    return search_result


def extract_postal_code_from_permalink(permalink: str):
    postal_code_pattern = re.compile('[0-9]{4}-[0-9]{5}')
    search_result = postal_code_pattern.search(permalink).group()
    return search_result


class HouseAddressInformation:
    state_name = ''
    postal_code = ''

    def __init__(self, s, p):
        self.state_name = s
        self.postal_code = p


def obj2dict(obj):
    return {
        'state_name': obj.state_name,
        'postal_code': obj.postal_code
    }


print(extract_address())

for item in extract_house_address_infos_from_permalink():
    print(json.dumps(item, default=obj2dict))

