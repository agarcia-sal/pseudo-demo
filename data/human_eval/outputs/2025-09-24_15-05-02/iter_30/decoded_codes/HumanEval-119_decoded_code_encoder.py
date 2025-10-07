from typing import List

def match_parens(lst: List[str]) -> str:
    def check(s: str) -> bool:
        val = 0
        for char in s:
            val += 1 if char == '(' else -1
            if val < 0:
                return False
        return val == 0

    if not lst or len(lst) < 2:
        return 'No'
    s1 = lst[0] + lst[1]
    s2 = lst[1] + lst[0]
    return 'Yes' if check(s1) or check(s2) else 'No'