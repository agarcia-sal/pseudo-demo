from typing import Callable

def solve(integer_N: int) -> str:
    def helper(index: int, acc: int) -> int:
        if index == len(str(integer_N)):
            return acc
        char_digit = str(integer_N)[index]
        num_digit = int(char_digit)
        return helper(index + 1, acc + num_digit)

    sum_acc = helper(0, 0)
    bin_str = ""
    bin_sum = bin(sum_acc)  # e.g., '0b101'
    i = 2  # skip the '0b' prefix
    while i < len(bin_sum):
        bin_str += bin_sum[i]
        i += 1
    return bin_str