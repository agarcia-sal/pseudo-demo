from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        acc_depth = 0
        peak_depth = 0
        idx = 0
        length = len(group_string)
        while idx < length:
            ch = group_string[idx]
            if ch == '(':
                acc_depth += 1
                if acc_depth > peak_depth:
                    peak_depth = acc_depth
            else:
                acc_depth -= 1
            idx += 1
        return peak_depth

    result_list: List[int] = []
    tokens = parentheses_string.split(' ')
    pos = 0
    length = len(tokens)
    while pos < length:
        element = tokens[pos]
        if element != '':
            temp_result = parse_paren_group(element)
            result_list.append(temp_result)
        pos += 1
    return result_list