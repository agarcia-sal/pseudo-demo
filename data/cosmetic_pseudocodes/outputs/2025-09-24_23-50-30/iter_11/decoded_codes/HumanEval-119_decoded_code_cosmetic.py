from typing import List

def match_parens(arr: List[str]) -> str:
    def check(s: str) -> bool:
        cnt = 0
        for ch in s:
            cnt += 1 if ch == '(' else -1
            if cnt < 0:
                return False
        return cnt == 0

    comboA = arr[0] + arr[1]
    comboB = arr[1] + arr[0]
    return 'Yes' if check(comboA) or check(comboB) else 'No'