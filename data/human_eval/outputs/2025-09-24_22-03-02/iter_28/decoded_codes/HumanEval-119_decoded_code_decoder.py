from typing import List

def match_parens(lst: List[str]) -> str:
    def check(s: str) -> bool:
        val = 0
        for i in range(len(s)):
            if s[i] == '(':
                val += 1
            else:
                val -= 1
            if val < 0:
                return False
        return val == 0

    s1 = lst[0] + lst[1]
    s2 = lst[1] + lst[0]
    if check(s1) or check(s2):
        return 'Yes'
    else:
        return 'No'