from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def recurse_chars(chars_list: List[str], index: int, max_val: int, current_val: int) -> int:
            if index == len(chars_list):
                return max_val
            c = chars_list[index]
            if c == '(':
                new_current = current_val + 1
                new_max = max(new_current, max_val)
                return recurse_chars(chars_list, index + 1, new_max, new_current)
            if c == ')':
                new_current = current_val - 1
                return recurse_chars(chars_list, index + 1, max_val, new_current)
            return recurse_chars(chars_list, index + 1, max_val, current_val)

        return recurse_chars(list(group_string), 0, 0, 0)

    raw_groups: List[str] = []
    temp_string = ""
    length = len(parentheses_string)
    for i in range(1, length + 2):  # 1-based indexing as per pseudocode, +1 extra to handle end
        if i <= length and parentheses_string[i - 1] != ' ':
            temp_string += parentheses_string[i - 1]
        else:
            if temp_string:
                raw_groups.append(temp_string)
                temp_string = ""

    filtered_groups: List[int] = []
    for group in raw_groups:
        if group != "":
            filtered_groups.append(parse_paren_group(group))

    return filtered_groups