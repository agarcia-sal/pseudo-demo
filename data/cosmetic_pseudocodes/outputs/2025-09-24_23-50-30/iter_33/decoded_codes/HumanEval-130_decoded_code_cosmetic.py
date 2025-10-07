from typing import List

def tri(n: int) -> List[int]:
    def loop(k: int, acc: List[int]) -> List[int]:
        if k > n:
            return acc
        is_even = (k % 2) == 0
        if is_even:
            updated_acc = acc + [(k // 2) + 1]
        else:
            updated_acc = acc + [acc[k - 1] + acc[k - 2] + ((k + 3) // 2)]
        return loop(k + 1, updated_acc)

    if n == 0:
        return [1]
    else:
        return loop(2, [1, 3])