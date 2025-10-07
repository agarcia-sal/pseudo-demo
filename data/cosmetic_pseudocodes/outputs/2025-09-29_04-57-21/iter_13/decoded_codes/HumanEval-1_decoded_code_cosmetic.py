from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: List[str] = []
    buffer_chars: List[str] = []
    depth_counter: int = 0

    def process_index(index: int) -> None:
        nonlocal depth_counter
        if index >= len(string_of_parentheses):
            return
        current_char = string_of_parentheses[index]
        if current_char == '(':
            depth_counter += 1
            buffer_chars.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_chars.append(current_char)
            if depth_counter == 0:
                results.append("".join(buffer_chars))
                buffer_chars.clear()
        process_index(index + 1)

    process_index(0)
    return results