from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_recorded = 0
        idx = 0
        while idx < len(group_string):
            ch = group_string[idx]
            if ch == '(':
                depth_counter += 1
                if max_depth_recorded < depth_counter:
                    max_depth_recorded = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return max_depth_recorded

    splitted_groups = parentheses_string.split(" ")
    result_collection: List[int] = []
    pos = 0
    while pos < len(splitted_groups):
        grp = splitted_groups[pos]
        if grp != "":
            result_collection.append(parse_paren_group(grp))
        pos += 1
    return result_collection