from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_tracker = 0
        deepest_level = 0
        i = 0
        while i < len(group_string):
            c = group_string[i]
            if c == '(':
                depth_tracker += 1
                if depth_tracker > deepest_level:
                    deepest_level = depth_tracker
            else:
                depth_tracker -= 1
            i += 1
        return deepest_level

    results: List[int] = []
    split_groups = parentheses_string.split(' ')
    for element in split_groups:
        if element != '':
            results.append(parse_paren_group(element))
    return results