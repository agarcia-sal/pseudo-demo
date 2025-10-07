from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    accumulator: List[str] = []
    segment: List[str] = []
    depth_counter: int = 0
    index_pointer: int = 0

    while index_pointer < len(string_of_parentheses):
        current_char: str = string_of_parentheses[index_pointer]

        if current_char == '(':
            depth_counter += 1
            segment.append(current_char)
        elif current_char == ')':
            segment.append(current_char)
            depth_counter -= 1
            if depth_counter == 0:
                accumulator.append(''.join(segment))
                segment.clear()
        # default case: no action

        index_pointer += 1

    return accumulator