def solve(integer_N: int) -> str:
    def sum_digits_recursive(str_digits: str, idx: int, acc: int) -> int:
        if idx >= len(str_digits):
            return acc
        return sum_digits_recursive(str_digits, idx + 1, acc + int(str_digits[idx]))

    str_number: str = str(integer_N)
    total_sum: int = sum_digits_recursive(str_number, 0, 0)
    binary_str_full: str = bin(total_sum)
    return binary_str_full[2:]