from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_counter = 0
        for symbol in group_string:
            if symbol == '(':
                depth_counter += 1
                if max_depth_counter < depth_counter:
                    max_depth_counter = depth_counter
            else:
                depth_counter -= 1
        return max_depth_counter

    substrings = [s for s in parentheses_string.split(' ') if s != '']
    result_list: List[int] = []
    for element in substrings:
        result_list.append(parse_paren_group(element))
    return result_list