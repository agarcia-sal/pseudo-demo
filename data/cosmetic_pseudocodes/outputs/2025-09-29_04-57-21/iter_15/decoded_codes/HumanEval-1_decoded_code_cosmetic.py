from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collector: List[str] = []
    temp_storage: List[str] = []
    depth_counter: int = 0
    idx: int = 0

    while idx < len(string_of_parentheses):
        current_char = string_of_parentheses[idx]

        if not (current_char != '('):
            depth_counter += 1
            temp_storage.append(current_char)
        elif not (current_char != ')'):
            depth_counter -= 1
            temp_storage.append(current_char)

            if not (depth_counter != 0):
                result_collector.append(''.join(temp_storage))
                temp_storage = []
        idx += 1

    return result_collector