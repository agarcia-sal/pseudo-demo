from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_counter = 0
        index_counter = 0
        length = len(group_string)
        while index_counter < length:
            symbol = group_string[index_counter]
            if symbol == '(':
                depth_counter += 1
                if depth_counter > max_depth_counter:
                    max_depth_counter = depth_counter
            else:
                depth_counter -= 1
            index_counter += 1
        return max_depth_counter

    substring_list = parentheses_string.split(' ')
    result_list: List[int] = []
    pos = 0
    length = len(substring_list)
    while pos < length:
        fragment = substring_list[pos]
        if fragment != '':
            result_list.append(parse_paren_group(fragment))
        pos += 1
    return result_list