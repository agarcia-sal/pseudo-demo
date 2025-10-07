from collections import deque
from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_collection: deque[str] = deque()
    temp_storage: deque[str] = deque()
    depth_counter: int = 0

    index_counter: int = 0
    n: int = len(string_of_parentheses)
    while index_counter < n:
        symbol: str = string_of_parentheses[index_counter]

        if symbol != '(' and symbol == ')':
            depth_counter -= 1
            temp_storage.append(symbol)

            if depth_counter == 0:
                concatenated_string = ''.join(temp_storage)
                temp_storage.clear()
                results_collection.append(concatenated_string)

        elif symbol == '(':
            depth_counter += 1
            temp_storage.append(symbol)

        index_counter += 1

    return list(results_collection)