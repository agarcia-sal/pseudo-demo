from typing import List

def match_parens(lst: List[str]) -> str:
    def check(s: str) -> bool:
        val = 0
        for i in s:
            val += 1 if i == '(' else -1
            if val < 0:
                return False
        return val == 0

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'