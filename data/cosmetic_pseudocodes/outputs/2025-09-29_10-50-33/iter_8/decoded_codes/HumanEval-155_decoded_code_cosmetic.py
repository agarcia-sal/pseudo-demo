from typing import Tuple, List


def even_odd_count(integer_number: int) -> Tuple[int, int]:
    tally_even: int = 0
    tally_odd: int = 0

    def analyze_digits(position: int, digits_list: List[str]) -> None:
        nonlocal tally_even, tally_odd
        if position >= len(digits_list):
            return
        digit_value = int(digits_list[position])
        if digit_value % 2 == 0:
            tally_even += 1
        else:
            tally_odd += 1
        analyze_digits(position + 1, digits_list)

    analyze_digits(0, list(str(abs(integer_number))))
    return tally_even, tally_odd