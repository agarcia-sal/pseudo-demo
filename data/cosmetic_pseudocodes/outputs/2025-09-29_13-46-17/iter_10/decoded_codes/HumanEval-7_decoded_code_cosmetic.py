from collections import deque
from typing import List, Deque

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> Deque[str]:
    queue: Deque[str] = deque()
    index: int = 0
    length: int = len(list_of_strings)

    while index < length:
        if substring_value in list_of_strings[index]:
            queue.append(list_of_strings[index])
        index += 1

    return queue