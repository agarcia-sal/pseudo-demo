from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(pat_string: str) -> int:
        x: int = 0
        y: int = 0
        for c in pat_string:
            if c == '(':
                x += 1
                if y < x:
                    y = x
            elif c == ')':
                x -= 1
        return y

    z: List[int] = []
    for q in parentheses_string.split(" "):
        if q != "":
            z.append(parse_paren_group(q))
    return z