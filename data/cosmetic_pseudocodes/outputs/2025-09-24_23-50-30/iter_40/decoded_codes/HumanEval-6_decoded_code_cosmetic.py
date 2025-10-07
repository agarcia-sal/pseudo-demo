from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(hgroup: str) -> int:
        zmax = 0
        zcur = 0
        for qchar in hgroup:
            if qchar == '(':
                zcur += 1
                if zcur > zmax:
                    zmax = zcur
            elif qchar == ')':
                zcur -= 1
        return zmax

    splist = parentheses_string.split(" ")
    ress: List[int] = []
    for xg in splist:
        if xg != "":
            ress.append(parse_paren_group(xg))
    return ress