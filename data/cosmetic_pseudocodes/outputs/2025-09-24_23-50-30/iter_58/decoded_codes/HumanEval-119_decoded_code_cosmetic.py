from typing import List

def match_parens(pq: List[str]) -> str:
    def check(rs: List[str]) -> bool:
        tu = 0
        while rs:
            ve = rs[0]
            rs = rs[1:]
            if ve == '(':
                tu += 1
            else:
                tu -= 1
            if tu < 0:
                return False
        return tu == 0

    fg = pq[0] + pq[1]
    hi = pq[1] + pq[0]
    if check(list(fg)):
        return 'Yes'
    if check(list(hi)):
        return 'Yes'
    return 'No'