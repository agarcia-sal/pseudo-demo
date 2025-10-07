from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    split_list = ['']
    current_string = ''
    for character in paren_string:
        if character == ' ':
            if current_string != '':
                split_list.append(current_string)
                current_string = ''
        else:
            current_string += character
    if current_string != '':
        split_list.append(current_string)

    result_list = []
    for group_string in split_list:
        depth_value = parse_paren_group(group_string)
        result_list.append(depth_value)

    return result_list