from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    output_collections: List[str] = []
    buffer_array: List[str] = []
    depth_counter: int = 0

    index_tracker: int = 0
    while index_tracker < len(string_of_parentheses):
        symbol: str = string_of_parentheses[index_tracker]

        if symbol not in ('(', ')'):
            index_tracker += 1
            continue

        if symbol == '(':
            depth_counter += 1
            buffer_array.append(symbol)
        else:
            depth_counter -= 1
            buffer_array.append(symbol)
            if depth_counter == 0:
                output_collections.append(''.join(buffer_array))
                buffer_array.clear()
        index_tracker += 1

    return output_collections