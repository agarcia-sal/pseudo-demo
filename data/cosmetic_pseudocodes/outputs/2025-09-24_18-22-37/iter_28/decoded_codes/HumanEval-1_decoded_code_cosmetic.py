from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collector_results: List[str] = []
    buffer_chars: List[str] = []
    depth_counter: int = 0
    index_iter: int = 0
    length_input: int = len(string_of_parentheses)

    while index_iter < length_input:
        current_char: str = string_of_parentheses[index_iter]

        if current_char == '(':
            depth_counter += 1
            buffer_chars.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_chars.append(current_char)
            if depth_counter == 0:
                group_string: str = ''
                pos: int = 0
                while pos < len(buffer_chars):
                    group_string += buffer_chars[pos]
                    pos += 1
                collector_results.append(group_string)
                buffer_chars.clear()
        else:
            pass  # Non-parenthesis characters ignored

        index_iter += 1

    return collector_results