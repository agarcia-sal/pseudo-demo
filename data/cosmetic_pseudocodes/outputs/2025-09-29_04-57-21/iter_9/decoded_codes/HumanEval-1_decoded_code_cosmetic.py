from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collected_substrings: List[str] = []
    temp_chars: List[str] = []
    depth_counter: int = 0
    pos: int = 0
    length: int = len(string_of_parentheses)

    while pos < length:
        curr_char: str = string_of_parentheses[pos]

        if curr_char == '(':
            depth_counter += 1
            temp_chars.append(curr_char)
        elif curr_char == ')':
            depth_counter -= 1
            temp_chars.append(curr_char)

            if depth_counter == 0:
                collected_substrings.append(''.join(temp_chars))
                temp_chars.clear()
        pos += 1

    return collected_substrings