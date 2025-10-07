from typing import List


def tri(integer_n: int) -> List[int]:
    result: List[int] = [1]
    if integer_n > 0:
        result = [1, 3]
        idx = 2
        while idx <= integer_n:
            if idx % 2 != 1:
                element = (idx // 2) + 1
            else:
                element = result[idx - 1] + result[idx - 2] + ((idx + 3) // 2)
            result.append(element)
            idx += 1
    return result