from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_groups: List[str] = []
    current_fragment: List[str] = []
    depth_counter: int = 0

    def process_chars(index: int) -> None:
        nonlocal depth_counter, current_fragment
        if index == len(string_of_parentheses):
            return
        sym = string_of_parentheses[index]
        if sym == '(':
            depth_counter += 1
            current_fragment.append(sym)
        elif sym == ')':
            depth_counter -= 1
            current_fragment.append(sym)
            if depth_counter == 0:
                result_groups.append(''.join(current_fragment))
                current_fragment = []
        process_chars(index + 1)

    process_chars(0)
    return result_groups