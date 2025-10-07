from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: List[str] = []
    buffer: List[str] = []
    depth_counter: int = 0

    idx: int = 0
    while idx < len(string_of_parentheses):
        char: str = string_of_parentheses[idx]

        if char == '(':
            depth_counter += 1
            buffer.append(char)
        elif char == ')':
            depth_counter -= 1
            buffer.append(char)

            if depth_counter == 0:
                grouped_string: str = "".join(buffer)
                results.append(grouped_string)
                buffer.clear()
        # default case: do nothing

        idx += 1

    return results