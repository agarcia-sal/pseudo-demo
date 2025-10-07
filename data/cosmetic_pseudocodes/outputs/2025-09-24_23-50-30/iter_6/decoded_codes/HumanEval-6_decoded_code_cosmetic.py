from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        highest_depth = 0
        index_counter = 0
        while index_counter < len(group_string):
            symbol = group_string[index_counter]
            if symbol == '(':
                depth_counter += 1
                if depth_counter > highest_depth:
                    highest_depth = depth_counter
            else:
                depth_counter -= 1
            index_counter += 1
        return highest_depth

    splitted_groups: List[str] = []
    temp_str = ""
    char_index = 0
    while char_index < len(parentheses_string):
        c = parentheses_string[char_index]
        if c != ' ':
            temp_str += c
        elif len(temp_str) > 0:
            splitted_groups.append(temp_str)
            temp_str = ""
        char_index += 1
    if len(temp_str) > 0:
        splitted_groups.append(temp_str)

    result_list: List[int] = []
    grp_index = 0
    while grp_index < len(splitted_groups):
        candidate_group = splitted_groups[grp_index]
        if candidate_group != "":
            result_list.append(parse_paren_group(candidate_group))
        grp_index += 1

    return result_list