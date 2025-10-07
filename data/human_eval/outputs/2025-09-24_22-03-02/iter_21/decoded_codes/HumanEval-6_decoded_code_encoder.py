from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    result: List[int] = []
    split_list: List[str] = []
    current_string = ""
    for current_char in paren_string:
        if current_char == ' ':
            if current_string:
                split_list.append(current_string)
                current_string = ""
        else:
            current_string += current_char
    if current_string:
        split_list.append(current_string)

    for x in split_list:
        result.append(parse_paren_group(x))

    return result