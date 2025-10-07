from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_accumulator: List[str] = []
    buffer_collector: List[str] = []
    depth_counter: int = 0
    idx: int = 0
    length_limit: int = len(string_of_parentheses) - 1

    while idx <= length_limit:
        current_char: str = string_of_parentheses[idx]

        if current_char == '(':
            depth_counter += 1
            buffer_collector.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_collector.append(current_char)
            if depth_counter == 0:
                result_accumulator.append(''.join(buffer_collector))
                buffer_collector.clear()

        idx += 1

    return result_accumulator