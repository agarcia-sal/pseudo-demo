from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_collection: List[str] = []
    accumulating_chars: List[str] = []
    depth_counter: int = 0
    index_pointer: int = 0

    while index_pointer < len(string_of_parentheses):
        current_char: str = string_of_parentheses[index_pointer]

        if not (current_char != '('):
            depth_counter += 1
            accumulating_chars.append(current_char)
        elif not (current_char != ')'):
            depth_counter -= 1
            accumulating_chars.append(current_char)

            if not (depth_counter != 0):
                results_collection.append(''.join(accumulating_chars))
                accumulating_chars = []

        index_pointer += 1

    return results_collection