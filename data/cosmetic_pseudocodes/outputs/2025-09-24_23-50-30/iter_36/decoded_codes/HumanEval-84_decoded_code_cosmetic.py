from typing import List

def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_chars: List[str] = list(str(integer_N))

    def helper(index: int, running_total: int) -> int:
        if index == len(digit_chars):
            return running_total
        else:
            return helper(index + 1, running_total + int(digit_chars[index]))

    total_sum: int = helper(0, accumulator)
    full_binary: str = bin(total_sum)
    result_binary: str = full_binary[2:]
    return result_binary