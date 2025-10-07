from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collection_segments: List[str] = []
    buffer_sequence: List[str] = []
    depth_counter: int = 0
    index_position: int = 0

    while index_position < len(string_of_parentheses):
        current_symbol: str = string_of_parentheses[index_position]

        if current_symbol == '(':
            depth_counter += 1
            buffer_sequence.append(current_symbol)

        elif current_symbol == ')':
            depth_counter -= 1
            buffer_sequence.append(current_symbol)

            if depth_counter == 0:
                collection_segments.append("".join(buffer_sequence))
                buffer_sequence.clear()

        index_position += 1

    return collection_segments