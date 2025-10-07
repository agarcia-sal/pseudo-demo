from typing import Sequence

def exchange(container_alpha: Sequence[int], container_beta: Sequence[int]) -> str:
    def tally_odd(index: int, limit: int, acc: int) -> int:
        if index >= limit:
            return acc
        # Check if container_alpha[index] is odd using bitwise operation for clarity and efficiency
        if (container_alpha[index] & 1) == 1:
            return tally_odd(index + 1, limit, acc + 1)
        else:
            return tally_odd(index + 1, limit, acc)

    def tally_even(index: int, limit: int, acc: int) -> int:
        if index >= limit:
            return acc
        # Check if container_beta[index] is even
        if (container_beta[index] & 1) == 0:
            return tally_even(index + 1, limit, acc + 1)
        else:
            return tally_even(index + 1, limit, acc)

    count_a = tally_odd(0, len(container_alpha), 0)
    count_b = tally_even(0, len(container_beta), 0)

    return "YES" if count_b >= count_a else "NO"