from typing import List

def parse_nested_parens(parens_input: str) -> List[int]:
    def parse_paren_group(sub_string: str) -> int:
        depth_counter = 0
        depth_max = 0
        for symbol in sub_string:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > depth_max:
                    depth_max = depth_counter
            elif symbol == ')':
                depth_counter -= 1
        return depth_max

    split_groups: List[str] = []
    temp_str = ""
    char_index = 0
    length = len(parens_input)
    while char_index <= length:
        if char_index == length or parens_input[char_index] == ' ':
            if temp_str:
                split_groups.append(temp_str)
                temp_str = ""
        else:
            temp_str += parens_input[char_index]
        char_index += 1

    result_list: List[int] = []
    group_counter = 0
    while group_counter < len(split_groups):
        current_entry = split_groups[group_counter]
        if current_entry:
            result_list.append(parse_paren_group(current_entry))
        group_counter += 1

    return result_list