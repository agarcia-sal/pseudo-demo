from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def contains_only_odd_digits(number: int) -> bool:
        digits_collection = str(number)
        for character in digits_collection:
            if int(character) % 2 == 0:
                return False
        return True

    filtered_numbers: List[int] = []

    def process_numbers(index: int) -> None:
        if index == len(list_of_positive_integers):
            return
        current_value = list_of_positive_integers[index]
        if contains_only_odd_digits(current_value):
            filtered_numbers.append(current_value)
        process_numbers(index + 1)

    process_numbers(0)
    return sorted(filtered_numbers)