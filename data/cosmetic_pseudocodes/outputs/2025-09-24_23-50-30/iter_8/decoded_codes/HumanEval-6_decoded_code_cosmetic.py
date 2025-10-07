from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        max_val: int = 0
        cur_val: int = 0
        idx: int = 0
        while idx < len(group_string):
            ch: str = group_string[idx]
            if ch == '(':
                cur_val += 1
                if cur_val > max_val:
                    max_val = cur_val
            else:
                cur_val -= 1
            idx += 1
        return max_val

    split_groups: List[str] = []
    temp_str: str = ""
    for ch in parentheses_string:
        if ch == ' ':
            if temp_str:
                split_groups.append(temp_str)
                temp_str = ""
        else:
            temp_str += ch
    if temp_str:
        split_groups.append(temp_str)

    result: List[int] = []
    for grp in split_groups:
        if grp:
            result.append(parse_paren_group(grp))

    return result