from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    list_of_results: List[str] = []
    list_current_string: List[str] = []
    integer_current_depth: int = 0

    for char in string_of_parentheses:
        if char == '(':
            integer_current_depth += 1
            list_current_string.append(char)
        elif char == ')':
            integer_current_depth -= 1
            list_current_string.append(char)
            if integer_current_depth == 0:
                list_of_results.append("".join(list_current_string))
                list_current_string = []

    return list_of_results