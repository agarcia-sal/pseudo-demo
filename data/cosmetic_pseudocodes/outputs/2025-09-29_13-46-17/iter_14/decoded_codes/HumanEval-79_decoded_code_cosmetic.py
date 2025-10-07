from typing import List

def decimal_to_binary(decimal_number: int) -> str:
    prefix_suffix: str = "db"
    digits: List[int] = []
    n: int = decimal_number

    def inner_binary(n_next: int, acc: List[int]) -> List[int]:
        if n_next == 0:
            return acc
        bit: int = n_next % 2
        acc = [bit] + acc
        return inner_binary(n_next // 2, acc)

    binary_digits: List[int] = inner_binary(n, [])
    trimmed_digits: List[int] = binary_digits if len(binary_digits) <= 1 else binary_digits[1:]
    result: str = prefix_suffix + "".join(map(str, trimmed_digits)) + prefix_suffix
    return result