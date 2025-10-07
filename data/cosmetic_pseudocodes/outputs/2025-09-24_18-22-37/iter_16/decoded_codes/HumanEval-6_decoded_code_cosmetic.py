from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_reached = 0
        idx = 0
        while idx < len(group_string):
            current_char = group_string[idx]
            if current_char == '(':
                temp_depth = depth_counter + 1
                depth_counter = temp_depth
                if max_depth_reached < temp_depth:
                    max_depth_reached = temp_depth
            else:
                # Implicitly current_char is ')', decrease depth
                depth_counter -= 1
            idx += 1
        return max_depth_reached

    split_groups = parentheses_string.split(' ')
    result_list: List[int] = []
    for group_element in split_groups:
        if group_element != '':
            calc_depth = parse_paren_group(group_element)
            result_list.append(calc_depth)
    return result_list