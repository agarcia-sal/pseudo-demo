from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        max_depth_counter: int = 0
        index_counter: int = 0
        length_counter: int = len(group_string)
        while index_counter < length_counter:
            symbol = group_string[index_counter]
            if symbol == '(':
                depth_counter += 1
                if depth_counter > max_depth_counter:
                    max_depth_counter = depth_counter
            else:
                depth_counter -= 1
            index_counter += 1
        return max_depth_counter

    accumulated_groups: List[str] = []
    temp_string: str = ''
    position_counter: int = 0
    total_length: int = len(parentheses_string)
    while position_counter <= total_length:
        if position_counter == total_length or parentheses_string[position_counter] == ' ':
            if temp_string != '':
                accumulated_groups.append(temp_string)
            temp_string = ''
        else:
            temp_string += parentheses_string[position_counter]
        position_counter += 1

    result_collection: List[int] = []
    iter_counter: int = 0
    acc_length: int = len(accumulated_groups)
    while iter_counter < acc_length:
        item = accumulated_groups[iter_counter]
        if item != '':
            result_collection.append(parse_paren_group(item))
        iter_counter += 1

    return result_collection