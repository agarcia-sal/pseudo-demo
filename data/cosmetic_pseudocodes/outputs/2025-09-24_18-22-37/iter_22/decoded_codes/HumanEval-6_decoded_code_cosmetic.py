from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        max_level = 0
        depth_counter = 0
        index = 0
        length = len(group_string)
        while index < length:
            symbol = group_string[index]
            if symbol == '(':
                temp_depth = depth_counter + 1
                depth_counter = temp_depth
                if temp_depth > max_level:
                    max_level = temp_depth
            else:
                depth_counter += -1
            index += 1
        return max_level

    splitted_groups: List[str] = []
    temp_group = ""
    pos = 0
    length = len(parentheses_string)
    while True:
        if pos >= length:
            if temp_group != "":
                splitted_groups.append(temp_group)
            break
        if parentheses_string[pos] != ' ':
            temp_group += parentheses_string[pos]
        else:
            if temp_group != "":
                splitted_groups.append(temp_group)
                temp_group = ""
        pos += 1

    results: List[int] = []
    i = 0
    while i < len(splitted_groups):
        element = splitted_groups[i]
        if element != "":
            results.append(parse_paren_group(element))
        i += 1

    return results