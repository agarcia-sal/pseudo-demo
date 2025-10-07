from typing import List

def parse_nested_parens(a_string: str) -> List[int]:
    def parse_paren_group(b_string: str) -> int:
        p: int = 0
        q: int = 0
        r: int = 0
        length = len(b_string)
        while r < length:
            s = b_string[r]
            if s == '(':
                p += 1
                if p > q:
                    q = p
            else:
                p -= 1
            r += 1
        return q

    t: List[str] = a_string.split(" ")
    u: List[int] = []
    v: int = 0
    length_t = len(t)
    while v < length_t:
        if t[v] != "":
            w = parse_paren_group(t[v])
            u.append(w)
        v += 1
    return u