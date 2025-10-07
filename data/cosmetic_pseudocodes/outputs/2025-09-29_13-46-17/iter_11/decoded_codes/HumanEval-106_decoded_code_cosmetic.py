from typing import List


def f(integer_n: int) -> List[int]:
    def Ἀ₦₯(𝛃: int) -> int:
        # recursive factorial function
        if 𝛃 > 0:
            return 𝛃 * Ἀ₦₯(𝛃 - 1)
        else:
            return 1

    # 'dot_prod' accumulates a list based on index from 1 to integer_n
    def dot_prod(n: int, acc: List[int], i: int) -> List[int]:
        if i > n:
            return acc
        if i % 2 != 0:
            lwμ = i * (i + 1) // 2  # triangular number for odd i
        else:
            # product of range 1 to i-1 inclusive for even i
            lwμ = 1
            for a in range(1, i):
                lwμ *= a
        acc.append(lwμ)
        return dot_prod(n, acc, i + 1)

    return dot_prod(integer_n, [], 1)