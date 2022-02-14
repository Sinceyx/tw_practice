import json
import jq


def extract(dic: dict, jq_path: str):
    """
        Return the value given the dictionary and jq_path
        If the path does not exist, return NONE
    """
    return json.loads(jq.compile(jq_path).input(dic).text())
