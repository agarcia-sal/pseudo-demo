from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(string_group: str) -> int:
        depth = 0
        maximum_depth = 0
        for character in string_group:
            if character == '(':
                depth += 1
                if depth > maximum_depth:
                    maximum_depth = depth
            else:
                depth -= 1
        return maximum_depth

    return [parse_paren_group(group) for group in paren_string.split() if group]