from typing import List


def parse_nested_parens(expr_string: str) -> List[int]:
    def parse_paren_group(inner_expr: str) -> int:
        depth_counter: int = 0
        peak_depth: int = 0
        idx: int = 0  # zero-based indexing for Python strings

        while idx < len(inner_expr):
            ch: str = inner_expr[idx]
            if ch == '(':
                depth_counter += 1
                if peak_depth < depth_counter:
                    peak_depth = depth_counter
            elif ch == ')':
                depth_counter -= 1
            idx += 1
        return peak_depth

    split_list: List[str] = []
    temp_str: str = ""
    pos: int = 0
    len_expr: int = len(expr_string)

    while pos < len_expr:
        ch = expr_string[pos]
        if ch == ' ':
            if temp_str:
                split_list.append(temp_str)
                temp_str = ""
        else:
            temp_str += ch
        pos += 1
    if temp_str:
        split_list.append(temp_str)

    result_list: List[int] = []
    i: int = 0

    while i < len(split_list):
        elem = split_list[i]
        if len(elem) > 0:
            result_list.append(parse_paren_group(elem))
        i += 1

    return result_list