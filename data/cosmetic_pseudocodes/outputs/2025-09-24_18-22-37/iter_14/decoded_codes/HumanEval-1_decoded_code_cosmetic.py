from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    buffer_chars: List[str] = []
    depth_level: int = 0
    position_index: int = 0
    length_limit: int = len(string_of_parentheses)

    while position_index < length_limit:
        current_symbol: str = string_of_parentheses[position_index]

        if current_symbol == '(':
            depth_level += 1
            buffer_chars.append(current_symbol)
        elif current_symbol == ')':
            depth_level -= 1
            buffer_chars.append(current_symbol)
            if depth_level == 0:
                group_string: str = "".join(buffer_chars)
                result_collection.append(group_string)
                buffer_chars.clear()
        # for other characters, do nothing

        position_index += 1

    return result_collection