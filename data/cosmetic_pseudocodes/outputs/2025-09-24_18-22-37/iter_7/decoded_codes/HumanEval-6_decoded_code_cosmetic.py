from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_value = 0
        index_var = 0
        while index_var < len(group_string):
            char_val = group_string[index_var]
            if char_val == '(':
                depth_counter += 1
                if max_depth_value < depth_counter:
                    max_depth_value = depth_counter
            else:
                depth_counter -= 1
            index_var += 1
        return max_depth_value

    splitted_groups = parentheses_string.split(' ')
    result_list: List[int] = []
    pos = 0
    while pos < len(splitted_groups):
        item = splitted_groups[pos]
        if item != '':
            result_list.append(parse_paren_group(item))
        pos += 1
    return result_list