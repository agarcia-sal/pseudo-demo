from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: List[str] = []
    current_fragment: List[str] = []
    depth_counter: int = 0

    idx: int = 0
    length: int = len(string_of_parentheses)
    while idx < length:
        curr_char: str = string_of_parentheses[idx]

        if curr_char == '(':
            depth_counter += 1
            current_fragment.append(curr_char)

        elif curr_char == ')':
            depth_counter -= 1
            current_fragment.append(curr_char)

            if depth_counter == 0:
                results.append(''.join(current_fragment))
                current_fragment.clear()

        idx += 1

    return results