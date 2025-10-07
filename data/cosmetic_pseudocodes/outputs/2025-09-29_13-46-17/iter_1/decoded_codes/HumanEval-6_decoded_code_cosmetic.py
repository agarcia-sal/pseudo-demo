from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_reached = 0
        for character in group_string:
            if character == '(':
                depth_counter += 1
                if depth_counter > max_depth_reached:
                    max_depth_reached = depth_counter
            else:
                depth_counter -= 1
        return max_depth_reached

    group_list = [item for item in parentheses_string.split(' ') if item]
    return list(map(parse_paren_group, group_list))