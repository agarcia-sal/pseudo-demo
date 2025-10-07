from collections import Counter
from typing import List

def remove_duplicates(string_of_tokens: str) -> List[str]:
    registry: Counter[str] = Counter(string_of_tokens)
    filter_list: List[str] = [member for member in string_of_tokens if registry[member] <= 1]
    return filter_list