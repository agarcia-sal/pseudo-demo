from typing import List


def parse_nested_parens(abc: str) -> List[int]:
    def parse_paren_group(pqr: str) -> int:
        uv = 0
        wx = 0

        def recur(i: int) -> int:
            nonlocal uv, wx
            if i == len(pqr):
                return wx
            else:
                if pqr[i] == '(':
                    uv += 1
                    if uv > wx:
                        wx = uv
                else:
                    uv -= 1
                return recur(i + 1)

        return recur(0)

    yz: List[int] = []
    st = 0
    n = len(abc)
    while st < n:
        ed = st
        while ed < n and abc[ed] != ' ':
            ed += 1
        if ed > st:
            yz.append(parse_paren_group(abc[st:ed]))
        st = ed + 1
    return yz