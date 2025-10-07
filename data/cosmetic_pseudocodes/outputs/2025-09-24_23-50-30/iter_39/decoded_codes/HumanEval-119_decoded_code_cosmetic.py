from typing import List


def match_parens(input_array: List[str]) -> str:
    def check(substring: str) -> bool:
        acc = 0
        idx = 0
        while idx < len(substring):
            ch = substring[idx]
            idx += 1
            if ch == '(':
                acc += 1
            elif ch == ')':
                acc -= 1
            if acc < 0:
                return False
        return acc == 0

    mergedA = input_array[0] + input_array[1]
    mergedB = input_array[1] + input_array[0]

    if check(mergedA) or check(mergedB):
        return 'Yes'
    return 'No'