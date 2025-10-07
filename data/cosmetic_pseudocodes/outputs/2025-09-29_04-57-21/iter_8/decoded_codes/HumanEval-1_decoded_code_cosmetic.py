from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_collection: List[str] = []
    temp_chars: List[str] = []
    depth_counter: int = 0

    idx: int = 0
    while idx < len(string_of_parentheses):
        current_char: str = string_of_parentheses[idx]

        if current_char not in ('(', ')'):
            idx += 1
            continue

        if current_char == '(':
            depth_counter += 1
            temp_chars.append(current_char)
        else:
            depth_counter -= 1
            temp_chars.append(current_char)
            if depth_counter == 0:
                results_collection.append(''.join(temp_chars))
                temp_chars.clear()

        idx += 1

    return results_collection