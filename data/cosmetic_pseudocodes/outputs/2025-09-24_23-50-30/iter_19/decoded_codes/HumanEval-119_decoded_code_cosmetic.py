from typing import List


def match_parens(twinstrings: List[str]) -> str:
    def check(candidate: str) -> bool:
        acc = 0
        for symbol in candidate:
            acc += 1 if symbol == '(' else -1
            if acc < 0:
                return False
        return acc == 0

    x = twinstrings[1] + twinstrings[0]
    y = twinstrings[0] + twinstrings[1]
    return 'Yes' if check(y) or check(x) else 'No'