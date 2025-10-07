from typing import Iterable, List


def unique_digits(collection_of_values: Iterable[int]) -> List[int]:
    def check_all_odds(number: int) -> bool:
        if number == 0:
            return True
        digit = number % 10
        if digit % 2 == 0:
            return False
        return check_all_odds(number // 10)

    candidates = filter(check_all_odds, collection_of_values)
    output_sequence: List[int] = []
    for value in candidates:
        # Insert value maintaining ascending order using bisect for efficiency
        from bisect import insort
        insort(output_sequence, value)
    return output_sequence