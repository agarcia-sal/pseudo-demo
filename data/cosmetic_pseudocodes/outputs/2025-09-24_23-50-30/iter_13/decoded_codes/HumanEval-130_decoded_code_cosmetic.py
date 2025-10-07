from typing import List


def tri(m: int) -> List[int]:
    if m == 0:
        return [1]
    result: List[int] = [1, 3]
    k = 2
    while k <= m:
        if k % 2 == 0:
            val = (k // 2) + 1
            result.append(val)
        else:
            val = result[k - 1] + result[k - 2] + ((k + 3) // 2)
            result.append(val)
        k += 1
    return result