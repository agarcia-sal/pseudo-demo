from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_recorded = 0
        for symbol in group_string:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > max_depth_recorded:
                    max_depth_recorded = depth_counter
            else:
                depth_counter -= 1
        return max_depth_recorded

    group_collection: List[str] = []
    cursor = 0
    length = len(parentheses_string)
    while True:
        next_space = parentheses_string.find(' ', cursor)
        if next_space == -1:
            substring = parentheses_string[cursor:length]
            if substring:
                group_collection.append(substring)
            break
        token = parentheses_string[cursor:next_space]
        if token:
            group_collection.append(token)
        cursor = next_space + 1

    result_list: List[int] = [parse_paren_group(entry) for entry in group_collection]
    return result_list