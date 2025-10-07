from collections import deque
from typing import List


def all_prefixes(input_string: str) -> List[str]:
    collection: deque[str] = deque()
    counter: int = 0

    while counter < len(input_string):
        fragment: str = input_string[:counter + 1]
        collection.append(fragment)
        counter += 1

    result_list: List[str] = []
    for item in collection:
        result_list.append(item)

    return result_list