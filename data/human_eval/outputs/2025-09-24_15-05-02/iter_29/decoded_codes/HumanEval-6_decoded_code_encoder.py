from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(string_group: str) -> int:
        current_depth = 0
        maximum_depth = 0
        for char in string_group:
            if char == '(':
                current_depth += 1
                if current_depth > maximum_depth:
                    maximum_depth = current_depth
            else:
                current_depth -= 1
        return maximum_depth

    group_strings = paren_string.split(' ')
    result_list: List[int] = []
    for group_string in group_strings:
        if group_string:
            result_list.append(parse_paren_group(group_string))
    return result_list