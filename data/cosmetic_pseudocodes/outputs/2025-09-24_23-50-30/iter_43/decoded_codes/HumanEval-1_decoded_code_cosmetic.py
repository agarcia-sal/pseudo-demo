from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    sequence_result: List[str] = []
    buffer_temp: List[str] = []
    depth_counter: int = 0
    index_tracker: int = 0
    length_limit: int = len(string_of_parentheses)

    while index_tracker < length_limit:
        symbol_current: str = string_of_parentheses[index_tracker]

        if symbol_current == '(':
            depth_counter += 1
            buffer_temp.append(symbol_current)
        elif symbol_current == ')':
            depth_counter -= 1
            buffer_temp.append(symbol_current)
            if depth_counter == 0:
                sequence_result.append(''.join(buffer_temp))
                buffer_temp = []
        index_tracker += 1

    return sequence_result