from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(substring: str) -> int:
        depth_counter = 0
        highest_depth = 0
        idx = 0
        while idx < len(substring):
            sym = substring[idx]
            if sym == '(':
                depth_counter += 1
                if depth_counter > highest_depth:
                    highest_depth = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return highest_depth

    parts = parentheses_string.split(" ")
    result_collection: List[int] = []
    part_index = 0
    while part_index < len(parts):
        segment = parts[part_index]
        if len(segment) != 0:
            result_collection.append(parse_paren_group(segment))
        part_index += 1

    return result_collection