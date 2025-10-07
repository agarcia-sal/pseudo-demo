from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    list_of_results: List[str] = []
    list_current_string: List[str] = []
    integer_current_depth: int = 0

    for character in string_of_parentheses:
        if character == '(':
            integer_current_depth += 1
            list_current_string.append(character)
        elif character == ')':
            integer_current_depth -= 1
            list_current_string.append(character)
            if integer_current_depth == 0:
                group = ''.join(list_current_string)
                list_of_results.append(group)
                list_current_string = []
        else:
            continue

    return list_of_results