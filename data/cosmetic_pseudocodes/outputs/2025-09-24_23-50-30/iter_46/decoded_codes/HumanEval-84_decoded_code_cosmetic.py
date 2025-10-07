from typing import Callable


def solve(value_A: int) -> str:
    def compute_sum(index_M: int, accumulator_B: int) -> int:
        if not (index_M < len(str(value_A))):
            return accumulator_B
        else:
            # The switch true with only one case true is equivalent to this:
            char_C: str = str(value_A)[index_M]
            digit_D: int = int(char_C)
            return compute_sum(index_M + 1, accumulator_B + digit_D)

    total_E: int = compute_sum(0, 0)
    full_binary_F: str = "0b"
    full_binary_F += bin(total_E)[2:]
    return full_binary_F[2:]