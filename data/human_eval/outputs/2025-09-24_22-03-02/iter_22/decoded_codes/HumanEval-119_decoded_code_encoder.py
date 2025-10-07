from typing import List

def match_parens(lst: List[str]) -> str:
    def check(s: str) -> bool:
        val = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                val += 1
            else:
                val -= 1
            if val < 0:
                return False
            i += 1
        return val == 0

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    if check(S1) or check(S2):
        return 'Yes'
    else:
        return 'No'