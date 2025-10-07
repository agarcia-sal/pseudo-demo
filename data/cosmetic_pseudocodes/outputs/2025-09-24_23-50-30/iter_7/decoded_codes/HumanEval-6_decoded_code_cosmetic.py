from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def helper(index: int, depth_accum: int, max_accum: int) -> int:
            if index >= len(group_string):
                return max_accum

            if group_string[index] == '(':
                new_depth = depth_accum + 1
                new_max = max(max_accum, new_depth)
                return helper(index + 1, new_depth, new_max)
            else:
                return helper(index + 1, depth_accum - 1, max_accum)

        return helper(0, 0, 0)

    split_groups: List[str] = []
    temp_str = ""
    for pos in range(len(parentheses_string)):
        if parentheses_string[pos] == ' ':
            if temp_str:
                split_groups.append(temp_str)
            temp_str = ""
        else:
            temp_str += parentheses_string[pos]
    if temp_str:
        split_groups.append(temp_str)

    result_list: List[int] = []
    for element in split_groups:
        if element:
            result_list.append(parse_paren_group(element))

    return result_list