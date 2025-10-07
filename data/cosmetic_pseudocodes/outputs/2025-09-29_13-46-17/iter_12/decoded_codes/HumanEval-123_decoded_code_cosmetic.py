from typing import List


def get_odd_collatz(n: int) -> List[int]:
    def is_greater_than_one(x: int) -> bool:
        return x > 1

    def next_collatz(x: int) -> int:
        return x // 2 if x % 2 == 0 else 3 * x + 1

    omega: int = n
    alpha: List[int] = [] if omega % 2 == 0 else [omega]

    result_sequence: List[int] = alpha.copy()

    def trampoline(z: int) -> List[int]:
        if is_greater_than_one(z):
            eta = next_collatz(z)
            if eta % 2 == 1:
                result_sequence.append(eta)
            return trampoline(eta)
        else:
            return result_sequence

    full_sequence = trampoline(omega)
    unique_sorted_sequence = sorted(set(full_sequence))
    return unique_sorted_sequence