from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    buffer_container: List[str] = []
    depth_counter: int = 0

    index_tracker: int = 0
    length: int = len(string_of_parentheses)
    while index_tracker < length:
        symbol: str = string_of_parentheses[index_tracker]

        if symbol not in ('(', ')'):
            index_tracker += 1
            continue

        if symbol == '(':
            depth_counter += 1
            buffer_container.append(symbol)
        elif symbol == ')':
            depth_counter -= 1
            buffer_container.append(symbol)
            if depth_counter == 0:
                concatenated = ''.join(buffer_container)
                result_collection.append(concatenated)
                buffer_container.clear()

        index_tracker += 1

    return result_collection