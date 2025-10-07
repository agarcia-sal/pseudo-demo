from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    accumulator_groups: List[str] = []
    buffer_chars: List[str] = []
    depth_counter: int = 0

    index: int = 0
    length: int = len(string_of_parentheses)
    while index < length:
        current_char: str = string_of_parentheses[index]

        if current_char == '(':
            depth_counter += 1
            buffer_chars.append(current_char)
        else:
            if current_char == ')':
                depth_counter -= 1
                buffer_chars.append(current_char)

                if depth_counter == 0:
                    grouped_string = ''.join(buffer_chars)  # join buffered chars into a string
                    accumulator_groups.append(grouped_string)
                    buffer_chars.clear()

        index += 1

    return accumulator_groups