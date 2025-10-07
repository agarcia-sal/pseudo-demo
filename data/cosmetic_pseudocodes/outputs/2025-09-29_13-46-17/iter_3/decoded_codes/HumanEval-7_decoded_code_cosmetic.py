from typing import List

def filter_by_substring(listOfStrings: List[str], substringValue: str) -> List[str]:
    return [s for s in listOfStrings if substringValue in s]