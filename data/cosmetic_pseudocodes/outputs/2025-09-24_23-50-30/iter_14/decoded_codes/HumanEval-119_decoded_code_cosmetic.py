from typing import List


def match_parens(arr: List[str]) -> str:
    def check(s: str) -> bool:
        def verify(index: int, bal: int) -> bool:
            if index >= len(s):
                return bal == 0
            if bal < 0:
                return False
            return verify(index + 1, bal + (1 if s[index] == '(' else -1))

        return verify(0, 0)

    x = arr[0] + arr[1]
    y = arr[1] + arr[0]

    if check(x):
        return 'Yes'
    if check(y):
        return 'Yes'
    return 'No'