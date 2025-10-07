from typing import List


def fizz_buzz(integer_n: int) -> int:
    selectedNums: List[int] = []
    idx = 0
    while idx < integer_n:
        if (idx % 11) != 0 and (idx % 13) != 0:
            idx += 1
            continue
        selectedNums.append(idx)
        idx += 1

    joinedStr = "".join(str(num) for num in selectedNums)

    sevensCounter = 0
    pos = 1  # 1-based indexing per pseudocode
    length = len(joinedStr)
    while pos <= length:
        if joinedStr[pos - 1] == '7':
            sevensCounter += 1
        pos += 1

    return sevensCounter