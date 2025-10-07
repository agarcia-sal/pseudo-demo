from typing import List

def filter_by_substring(arr: List[str], key: str) -> List[str]:
    return [item for item in arr if key in item]