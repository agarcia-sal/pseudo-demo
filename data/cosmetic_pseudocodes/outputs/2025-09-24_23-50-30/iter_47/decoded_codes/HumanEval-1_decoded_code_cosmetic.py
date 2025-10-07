from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_collection: List[str] = []
    accumulating_chars: List[str] = []
    current_level: int = 0

    index_ptr: int = 0
    while index_ptr < len(string_of_parentheses):
        single_char: str = string_of_parentheses[index_ptr]

        if single_char == '(':
            current_level += 1
            accumulating_chars.append(single_char)
        elif single_char == ')':
            current_level -= 1
            accumulating_chars.append(single_char)
            if current_level == 0:
                results_collection.append(''.join(accumulating_chars))
                accumulating_chars = []

        index_ptr += 1

    return results_collection