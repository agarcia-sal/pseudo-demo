from functools import reduce
from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    def find_max_length(seq: List[str]) -> int:
        return reduce(lambda acc, elem: max(acc, len(elem)), seq, 0)

    if not list_of_strings:
        return None

    max_len = find_max_length(list_of_strings)
    idx = 0

    while idx < len(list_of_strings):
        current_str = list_of_strings[idx]
        if len(current_str) == max_len:
            return current_str
        idx += 1