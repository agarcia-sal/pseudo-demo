from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        current_depth = 0
        maximum_depth = 0
        for char in group_string:
            if char == '(':
                current_depth += 1
                if current_depth > maximum_depth:
                    maximum_depth = current_depth
            else:
                current_depth -= 1
        return maximum_depth

    groups = parentheses_string.split(" ")
    return [parse_paren_group(group) for group in groups if group]