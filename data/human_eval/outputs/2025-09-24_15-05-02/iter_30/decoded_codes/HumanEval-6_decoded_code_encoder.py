from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(string_group: str) -> int:
        depth = 0
        max_depth = 0
        for character in string_group:
            if character == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    return [parse_paren_group(x) for x in paren_string.split() if x]