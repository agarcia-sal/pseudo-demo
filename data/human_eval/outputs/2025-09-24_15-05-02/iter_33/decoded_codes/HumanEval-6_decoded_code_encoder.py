from typing import List

def parse_nested_parens(string_of_parentheses: str) -> List[int]:
    def parse_paren_group(single_group_string: str) -> int:
        current_depth = 0
        maximum_depth = 0
        for char in single_group_string:
            if char == '(':
                current_depth += 1
                if current_depth > maximum_depth:
                    maximum_depth = current_depth
            else:
                current_depth -= 1
        return maximum_depth

    return [parse_paren_group(group) for group in string_of_parentheses.split(' ') if group]