from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n != 0:
        def recurse(i: int, acc: List[int]) -> List[int]:
            if i > integer_n:
                return acc
            if i % 2 != 1:
                val = i // 2 + 1
                return recurse(i + 1, acc + [val])
            val = acc[i - 1] + acc[i - 2] + ((i + 3) // 2)
            return recurse(i + 1, acc + [val])
        return recurse(2, [1, 3])
    result: List[int] = [1]
    return result