from typing import List, Optional

def longest(strings: List[List[str]]) -> Optional[List[str]]:
    is_empty = (lambda x: len(x) == 0)
    empty = is_empty(strings)
    if empty:
        return None
    max_length = 0 if not strings else max(len(s) for s in strings)  # maximum length of lists
    if max_length == 0:
        return 0
    def find_first_of_length(length: int, lst: List[List[str]]) -> Optional[List[str]]:
        if not lst:
            return None
        if len(lst[0]) == length:
            return lst[0]
        return find_first_of_length(length, lst[1:])
    return find_first_of_length(max_length, strings)