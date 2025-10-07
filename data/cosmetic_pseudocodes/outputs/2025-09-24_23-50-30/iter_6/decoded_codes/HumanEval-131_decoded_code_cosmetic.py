from typing import List

def digits(m: str) -> int:
    acc: int = 1
    cnt: int = 0
    i: int = 0
    digits_list: List[str] = list(m)
    while i < len(digits_list):
        val: int = int(digits_list[i])
        if val % 2 != 0:
            acc *= val
            cnt += 1
        i += 1
    return 0 if cnt == 0 else acc