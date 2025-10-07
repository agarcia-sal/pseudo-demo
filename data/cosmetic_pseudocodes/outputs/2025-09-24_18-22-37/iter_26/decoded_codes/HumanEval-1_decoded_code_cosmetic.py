from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collection_accumulated: List[str] = []
    buffer_substring: List[str] = []
    depth_counter: int = 0
    index_counter: int = 0
    total_chars: int = len(string_of_parentheses)

    while index_counter < total_chars:
        current_char: str = string_of_parentheses[index_counter]

        if current_char == '(':
            depth_counter += 1
            buffer_substring.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_substring.append(current_char)

            if depth_counter == 0:
                assembled_string = ''.join(buffer_substring)
                collection_accumulated.append(assembled_string)
                buffer_substring.clear()
        # default: no operation for other characters

        index_counter += 1

    return collection_accumulated