from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    accumulated_results: List[str] = []
    collecting_chars: List[str] = []
    depth_counter: int = 0

    for char_element in string_of_parentheses:
        if char_element == '(':
            depth_counter += 1
            collecting_chars.append(char_element)
        elif char_element == ')':
            depth_counter -= 1
            collecting_chars.append(char_element)
            if depth_counter == 0:
                grouped_string = ''.join(collecting_chars)
                accumulated_results.append(grouped_string)
                collecting_chars.clear()

    return accumulated_results