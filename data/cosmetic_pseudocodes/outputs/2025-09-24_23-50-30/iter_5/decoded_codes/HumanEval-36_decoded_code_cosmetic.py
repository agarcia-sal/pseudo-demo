from typing import List


def fizz_buzz(integer_n: int) -> int:
    def gather_divisible(index: int, collected: List[int]) -> List[int]:
        if index >= integer_n:
            return collected
        if index % 11 == 0 or index % 13 == 0:
            return gather_divisible(index + 1, collected + [index])
        return gather_divisible(index + 1, collected)

    filtered_values = gather_divisible(0, [])
    combined_text = "".join(str(value) for value in filtered_values)

    total_count = 0
    idx = 0
    while idx < len(combined_text):
        if combined_text[idx] == "7":
            total_count += 1
        idx += 1

    return total_count