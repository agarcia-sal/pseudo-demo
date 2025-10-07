from typing import List

def separate_paren_groups(s: str) -> List[str]:
    res, cur, d = [], [], 0
    for c in s.replace(" ",""):
        if c == '(': 
            d += 1
            cur.append(c)
        elif c == ')': 
            d -= 1
            cur.append(c)
        if d == 0 and cur: 
            res.append("".join(cur))
            cur = []
    return res