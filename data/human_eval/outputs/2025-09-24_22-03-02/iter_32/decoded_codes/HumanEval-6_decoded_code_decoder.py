from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        index = 0
        length = len(s)
        while index < length:
            c = s[index]
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
                if depth < 0:
                    raise ValueError("Invalid parentheses: closing parenthesis without matching opening parenthesis")
            index += 1
        if depth != 0:
            raise ValueError("Invalid parentheses: unmatched opening parenthesis")
        return max_depth

    result: List[int] = []
    split_index = 0
    length_of_paren_string = len(paren_string)
    while split_index < length_of_paren_string:
        current_string = ""
        while split_index < length_of_paren_string and paren_string[split_index] != ' ':
            current_string += paren_string[split_index]
            split_index += 1
        if len(current_string) > 0:
            max_depth_value = parse_paren_group(current_string)
            result.append(max_depth_value)
        split_index += 1
    return result