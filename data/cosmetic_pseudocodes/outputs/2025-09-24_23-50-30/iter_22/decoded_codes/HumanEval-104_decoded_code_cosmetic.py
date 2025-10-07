from typing import Iterable, List, Set

def unique_digits(input_sequence: Iterable[int]) -> List[int]:
    collected_items: Set[int] = set()

    def check_all_digits_odd(number: int) -> bool:
        while number > 0:
            current_digit = number % 10
            if (current_digit % 2) == 0:
                return False
            number //= 10
        return True

    for element in input_sequence:
        if element > 0 and check_all_digits_odd(element):
            collected_items.add(element)

    sorted_result = list(collected_items)
    sorted_result.sort()
    return sorted_result