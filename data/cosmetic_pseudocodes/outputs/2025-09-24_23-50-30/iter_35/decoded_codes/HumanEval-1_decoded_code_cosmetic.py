from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_list: List[str] = []
    buffer_list: List[str] = []
    depth_count: int = 0
    index_ptr: int = 0

    while index_ptr < len(string_of_parentheses):
        current_char: str = string_of_parentheses[index_ptr]
        if current_char == '(':
            depth_count += 1
            buffer_list.append(current_char)
        elif current_char == ')':
            depth_count -= 1
            buffer_list.append(current_char)
            if depth_count == 0:
                results_list.insert(len(results_list), "".join(buffer_list))
                buffer_list.clear()
        # Non-parenthesis characters are ignored
        index_ptr += 1

    return results_list