from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(estr: str) -> int:
        d: int = 0  # current depth
        m: int = 0  # max depth found
        i: int = 0
        length: int = len(estr)
        while i < length:
            ch: str = estr[i]
            if ch == '(':
                d += 1
                if m < d:
                    m = d
            else:
                # According to pseudocode: if ch != '(' then d = d - 1
                # So presumably ch == ')', but no validation here.
                d -= 1
            i += 1
        return m

    parts: List[str] = []
    temp_str: str = ""
    j: int = 0
    length: int = len(parentheses_string)
    while j < length:
        c: str = parentheses_string[j]
        if c != ' ':
            temp_str += c
        else:
            if temp_str != "":
                parts.append(temp_str)
                temp_str = ""
        j += 1
    if temp_str != "":
        parts.append(temp_str)

    result: List[int] = []
    for k in range(len(parts)):
        if parts[k] != "":
            result.append(parse_paren_group(parts[k]))
    return result