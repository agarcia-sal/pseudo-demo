from typing import List


def digits(x: int) -> int:
    acc: int = 1
    counter: int = 0
    chars: List[str] = list(str(x))
    for idx in range(len(chars)):
        val: int = int(chars[idx])
        if val % 2 == 0:
            continue
        acc *= val
        counter += 1
    return 0 if counter == 0 else acc