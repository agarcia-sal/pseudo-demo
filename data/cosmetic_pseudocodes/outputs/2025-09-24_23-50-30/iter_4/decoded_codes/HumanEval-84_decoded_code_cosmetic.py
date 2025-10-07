from typing import List

def solve(integer_N: int) -> str:
    def helper(acc: int, digits_list: List[str]) -> int:
        if not digits_list:
            return acc
        else:
            return helper(acc + int(digits_list[0]), digits_list[1:])
    digits_array = list(str(integer_N))
    total_sum = helper(0, digits_array)
    # Convert total_sum to binary string, then remove the '0b' prefix
    result = bin(total_sum)[2:]
    return result