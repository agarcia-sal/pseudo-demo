from typing import Iterable, List

def unique_digits(collection_of_numbers: Iterable[int]) -> List[int]:
    filtered_numbers = set()
    for candidate_number in collection_of_numbers:
        is_only_odd_digits = True
        for digit_character in str(candidate_number):
            if int(digit_character) % 2 == 0:
                is_only_odd_digits = False
                break
        if is_only_odd_digits:
            filtered_numbers.add(candidate_number)
    result_list = list(filtered_numbers)
    result_list.sort()
    return result_list