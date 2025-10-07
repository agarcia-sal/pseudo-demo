from typing import List, Set

def unique_digits(sequence_of_positive_integers: List[int]) -> List[int]:
    def is_all_odd(number: int) -> bool:
        def check_digits(index: int) -> bool:
            if index < 0:
                return True
            current_digit = (number // (10 ** index)) % 10
            if current_digit % 2 != 1:
                return False
            return check_digits(index - 1)

        digit_count = 0
        temp_number = number
        while temp_number > 0:
            temp_number //= 10
            digit_count += 1
        return check_digits(digit_count - 1)

    filtered_set: Set[int] = set()
    index_counter = 0
    while index_counter < len(sequence_of_positive_integers):
        candidate_element = sequence_of_positive_integers[index_counter]
        if is_all_odd(candidate_element):
            filtered_set.add(candidate_element)
        index_counter += 1

    sorted_list = sorted(filtered_set)
    return sorted_list