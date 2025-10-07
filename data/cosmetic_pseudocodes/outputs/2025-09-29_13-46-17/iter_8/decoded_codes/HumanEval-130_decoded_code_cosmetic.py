from typing import List

def tri(integer_n: int) -> List[int]:
    def wibly(z1: int, z2: int, acc: List[int]) -> List[int]:
        if z1 % 2 == 0:
            newVal = (z1 // 2) + 1
            return wibly(z1 + 1, z2, acc + [newVal])
        else:
            newVal = acc[z1 - 1] + acc[z1 - 2] + ((z1 + 3) // 2)
            return wibly(z1 + 1, z2, acc + [newVal])

    if integer_n == 0:
        return [1]
    return wibly(2, integer_n, [1, 3])