from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    output_collection: List[str] = []
    buffer_container: List[str] = []
    depth_counter: int = 0

    index: int = 0
    length: int = len(string_of_parentheses)
    while index < length:
        current_ch: str = string_of_parentheses[index]

        if current_ch == '(':
            depth_counter += 1
            buffer_container.append(current_ch)
        elif current_ch == ')':
            depth_counter -= 1
            buffer_container.append(current_ch)
            if depth_counter == 0:
                output_collection.append(''.join(buffer_container))
                buffer_container = []

        index += 1

    return output_collection