from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: List[str] = []
    buffer: List[str] = []
    depth_counter: int = 0

    for char in string_of_parentheses:
        if char == '(':
            depth_counter += 1
            buffer.append(char)
        elif char == ')':
            depth_counter -= 1
            buffer.append(char)

            if depth_counter == 0:
                results.append(''.join(buffer))
                buffer.clear()

    return results