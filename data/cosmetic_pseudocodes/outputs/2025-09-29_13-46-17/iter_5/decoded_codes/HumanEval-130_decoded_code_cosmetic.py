from typing import List

def tri(integer_n: int) -> List[int]:
    def recurse(k: int, acc: List[int]) -> List[int]:
        if k > integer_n:
            return acc
        # Compute new_val based on parity of k
        mod_k = k % 2
        if mod_k == 1:
            new_val = acc[k - 1] + acc[k - 2] + ((k + 3) // 2)
        else:
            new_val = (k // 2) + 1
        return recurse(k + 1, acc + [new_val])

    if integer_n == 0:
        return [1]

    return recurse(2, [1, 3])