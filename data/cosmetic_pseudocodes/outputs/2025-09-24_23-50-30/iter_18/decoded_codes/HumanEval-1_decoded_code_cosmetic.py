from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_accumulator: List[str] = []
    buffer_chars: List[str] = []
    depth_counter: int = 0
    index_pointer: int = 0

    while index_pointer < len(string_of_parentheses):
        curr_symbol: str = string_of_parentheses[index_pointer]

        if curr_symbol not in ('(', ')'):
            index_pointer += 1
            continue

        if curr_symbol == '(':
            depth_counter += 1
            buffer_chars.append(curr_symbol)
            index_pointer += 1
            continue

        if curr_symbol == ')':
            depth_counter -= 1
            buffer_chars.append(curr_symbol)

            if depth_counter == 0:
                # Joining buffered chars into a single string when a complete group is closed
                assembled_string = ''.join(buffer_chars)
                results_accumulator.append(assembled_string)
                buffer_chars = []

            index_pointer += 1
            continue

    return results_accumulator