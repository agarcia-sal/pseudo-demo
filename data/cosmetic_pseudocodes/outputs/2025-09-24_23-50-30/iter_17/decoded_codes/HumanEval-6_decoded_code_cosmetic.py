from typing import List


def parse_nested_parens(input_string: str) -> List[int]:
    def parse_paren_group(content: str) -> int:
        count_depth = 0
        max_depth_val = 0
        for symbol in content:
            if symbol == '(':
                count_depth += 1
                if max_depth_val < count_depth:
                    max_depth_val = count_depth
            elif symbol == ')':
                count_depth -= 1
        return max_depth_val

    split_groups: List[str] = []
    temp_str = ""
    i = 0
    n = len(input_string)
    while i < n:
        if input_string[i] != " ":
            temp_str += input_string[i]
        elif temp_str:
            split_groups.append(temp_str)
            temp_str = ""
        i += 1
    if temp_str:
        split_groups.append(temp_str)

    depths_list: List[int] = [parse_paren_group(subgroup) for subgroup in split_groups]
    return depths_list