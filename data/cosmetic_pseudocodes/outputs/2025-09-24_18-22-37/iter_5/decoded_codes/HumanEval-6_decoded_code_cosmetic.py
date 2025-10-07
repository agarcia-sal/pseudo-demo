from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        max_depth_var = 0
        depth_counter = 0
        index_counter = 0
        while index_counter < len(group_string):
            current_char = group_string[index_counter]
            if current_char == '(':
                depth_counter += 1
                if depth_counter > max_depth_var:
                    max_depth_var = depth_counter
            else:
                depth_counter -= 1
            index_counter += 1
        return max_depth_var

    split_groups: List[str] = []
    temp_string = ""
    i = 0
    while i < len(parentheses_string):
        if parentheses_string[i] == ' ':
            if temp_string != "":
                split_groups.append(temp_string)
                temp_string = ""
        else:
            temp_string += parentheses_string[i]
        i += 1
    if temp_string != "":
        split_groups.append(temp_string)

    result_collection: List[int] = []
    for element in split_groups:
        if element != "":
            result_collection.append(parse_paren_group(element))
    return result_collection