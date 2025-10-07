from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    array_of_results: List[str] = []
    buffer_of_chars: List[str] = []
    depth_counter: int = 0

    def traverse(index: int) -> None:
        nonlocal depth_counter
        if index >= len(string_of_parentheses):
            return
        current_char = string_of_parentheses[index]
        if current_char == '(':
            depth_counter += 1
            buffer_of_chars.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_of_chars.append(current_char)
            if depth_counter == 0:
                array_of_results.append(''.join(buffer_of_chars))
                buffer_of_chars.clear()
        # ignore other characters
        traverse(index + 1)

    traverse(0)
    return array_of_results