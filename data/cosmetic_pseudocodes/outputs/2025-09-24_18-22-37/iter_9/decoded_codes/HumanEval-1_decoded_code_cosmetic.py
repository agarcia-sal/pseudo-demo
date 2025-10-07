from typing import List


def separate_paren_groups(input_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    accumulating_chars: List[str] = []
    depth_counter: int = 0
    idx: int = 0

    while idx < len(input_parentheses):
        current_char: str = input_parentheses[idx]

        if current_char == '(':
            depth_counter += 1
            accumulating_chars.append(current_char)

        elif current_char == ')':
            depth_counter -= 1
            accumulating_chars.append(current_char)

            if depth_counter == 0:
                concatenated_str = ''.join(accumulating_chars)
                result_collection.append(concatenated_str)
                accumulating_chars.clear()

        idx += 1

    return result_collection