"""
    A program to capture data from website: https://www.atrealty.com.au/
"""
import re
import json
import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extractor import extract


def crawl():
    website_data_json = json.loads(__fetch_website_data())
    full_address = __extract_full_house_address(website_data_json)
    return __format_house_address(full_address)


def __fetch_website_data():
    url = 'https://www.atrealty.com.au/wp-json/hi-api/v1/properties?page=1&per_page=5&listing=residential' \
          '&price_type=sale&tags_field=&search-id=983&auction=&inspection=&location=&sub_type=any&min_price' \
          '=&max_price=&min_bedrooms=&max_bedrooms=&min_bathrooms=&max_bathrooms=&parking=&surrounding_suburbs=1' \
          '&suburb=&state=&latlng='
    return requests.get(url).text


def __extract_full_house_address(data: json):
    full_address_array = []
    permalink_pattern = re.compile('/[a-z-0-9-]*[0-9]{4}-[0-9]{5}/$')
    for item in extract(data, '.data'):
        full_address_array.append(permalink_pattern.search(extract(item, '.permalink')).group().replace('/', ''))
    return full_address_array


def __format_house_address(address_array: list):
    result_address_array = []
    for ele in address_array:
        result_address = ''
        ele = ele.upper()
        result_address += __parse_house_number(ele) + ' '
        result_address += __parse_other_part(ele)
        result_address_array.append(result_address)
    return result_address_array


def __parse_house_number(address_str: str):
    house_number = re.compile('^[0-9]?-?[0-9]+').search(address_str).group()
    if '-' in house_number:
        return 'UNIT ' + house_number.replace('-', ' ')
    return house_number


def __parse_other_part(address_str: str):
    return re.compile('[A-Z][A-Z-]*-[0-9]{4}').search(address_str).group().replace('-', ' ')


print(crawl())

