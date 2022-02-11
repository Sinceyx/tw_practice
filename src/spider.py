"""
    A program to capture data from website: https://www.atrealty.com.au/
"""
import re
import json
import requests
from extractor import extract


class AtrealtyWebSpider(object):
    __url = 'https://www.atrealty.com.au/wp-json/hi-api/v1/properties?page=1&per_page=12&listing=residential' \
            '&price_type=sale&tags_field=&search-id=983&auction=&inspection=&location=&sub_type=any&min_price' \
            '=&max_price=&min_bedrooms=&max_bedrooms=&min_bathrooms=&max_bathrooms=&parking=&surrounding_suburbs=1' \
            '&suburb=&state=&latlng= '
    page_size = 5
    data_array = {}

    def __init__(self, p):
        self.page_size = p
        self.data_array = self.__capture_product_infos_from_atrealty(p)

    def __capture_product_infos_from_atrealty(self, page_size: int):
        result = json.loads(requests.get(self.__url.replace('per_page=12', 'per_page='+str(page_size))).text)
        return extract(result, '.data')


def extract_address(arealty_web_spider: AtrealtyWebSpider):
    address_array = []
    for item in arealty_web_spider.data_array:
        address_array.append(extract(item, '.name'))
    return address_array


def extract_house_address_infos(arealty_web_spider: AtrealtyWebSpider):
    state_name_array = []
    postal_codes_array = []
    permalink_array = []
    for item in arealty_web_spider.data_array:
        permalink = extract(item, '.permalink')
        permalink_array.append(permalink)
        permalink_pattern = re.compile('/?[^./][0-9a-z-]*/?$')
        permalink_regex_search_result = permalink_pattern.search(permalink).group().replace('/', '')
        state_name_array.append(__extract_state_name_from_permalink(permalink_regex_search_result))
        postal_codes_array.append(__extract_postal_code_from_permalink(permalink_regex_search_result))
    house_info_array = {'state_names': state_name_array, 'postal_codes': postal_codes_array, 'permalinks': permalink_array }
    return house_info_array


def __extract_state_name_from_permalink(permalink: str):
    state_name_pattern = re.compile('^[1-9]?[0-9-]*[a-z-0-9]*[a-z]')
    search_result = state_name_pattern.search(permalink).group()
    return search_result


def __extract_postal_code_from_permalink(permalink: str):
    postal_code_pattern = re.compile('[0-9]{4}-[0-9]{5}')
    search_result = postal_code_pattern.search(permalink).group()
    return search_result
