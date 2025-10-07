from typing import List

def fizz_buzz(integer_n: int) -> int:
    accumulator: List[int] = []

    def collect(divisor_candidate: int, accumulator_list: List[int], limit: int, current_index: int) -> None:
        if current_index == limit:
            return
        # Include current_index if it is divisible by 11 or 13
        if not (current_index % 11 != 0 and current_index % 13 != 0):
            accumulator_list.append(current_index)
        collect(divisor_candidate, accumulator_list, limit, current_index + 1)

    collect(0, accumulator, integer_n, 0)
    combined_chars = "".join(str(element) for element in accumulator)
    sevens_total = combined_chars.count('7')
    return sevens_total