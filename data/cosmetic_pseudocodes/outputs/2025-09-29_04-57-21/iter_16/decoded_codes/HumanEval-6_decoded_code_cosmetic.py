from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        highest_depth = 0
        iterator = 0
        while iterator < len(group_string):
            symbol = group_string[iterator]
            if symbol == '(':
                depth_counter += 1
                if depth_counter > highest_depth:
                    highest_depth = depth_counter
            else:
                depth_counter -= 1
            iterator += 1
        return highest_depth

    segment_list = parentheses_string.split(' ')
    result_collection: List[int] = []
    index_counter = 0
    while index_counter < len(segment_list):
        current_segment = segment_list[index_counter]
        if current_segment != '':
            result_collection.append(parse_paren_group(current_segment))
        index_counter += 1
    return result_collection