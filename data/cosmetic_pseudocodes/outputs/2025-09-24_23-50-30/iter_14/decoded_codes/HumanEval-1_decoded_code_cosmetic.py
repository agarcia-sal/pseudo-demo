from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    group_chars: List[str] = []
    depth_counter: int = 0

    position: int = 0
    length: int = len(string_of_parentheses)
    while position < length:
        current_symbol: str = string_of_parentheses[position]

        if current_symbol == '(':
            depth_counter += 1
            group_chars.append(current_symbol)
        elif current_symbol == ')':
            depth_counter -= 1
            group_chars.append(current_symbol)

            if depth_counter == 0:
                result_collection.append(''.join(group_chars))
                group_chars = []
        position += 1

    return result_collection