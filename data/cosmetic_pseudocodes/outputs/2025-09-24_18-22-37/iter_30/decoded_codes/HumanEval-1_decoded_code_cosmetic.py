from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_groups: List[str] = []
    active_chars: List[str] = []
    depth_level: int = 0
    index_counter: int = 0
    total_length: int = len(string_of_parentheses)

    while index_counter < total_length:
        current_symbol: str = string_of_parentheses[index_counter]

        if current_symbol == '(':
            depth_level += 1  # + (1 + 0) simplified to +1
            active_chars.append(current_symbol)
        elif current_symbol == ')':
            depth_level -= 1
            active_chars.append(current_symbol)

            if depth_level == 0:
                joined_group: str = "".join(active_chars)
                result_groups.append(joined_group)
                active_chars.clear()

        index_counter += 1

    return result_groups