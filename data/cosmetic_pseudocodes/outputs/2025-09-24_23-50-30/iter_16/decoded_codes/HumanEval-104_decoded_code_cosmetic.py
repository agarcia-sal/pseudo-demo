from typing import List

def unique_digits(collection_positive_ints: List[int]) -> List[int]:
    def is_odd_only(number: int, accumulator: int) -> bool:
        digits_str = str(number)
        if accumulator == len(digits_str):
            return True
        digit_num = int(digits_str[accumulator])
        return (digit_num % 2 != 0) and is_odd_only(number, accumulator + 1)

    result_collection: List[int] = []
    index = 0
    while index < len(collection_positive_ints):
        current_num = collection_positive_ints[index]
        if is_odd_only(current_num, 0):
            result_collection.append(current_num)
        index += 1

    sorted_result: List[int] = []
    unsorted_values = result_collection.copy()
    while unsorted_values:
        min_value = unsorted_values[0]
        pos = 1
        while pos < len(unsorted_values):
            if unsorted_values[pos] < min_value:
                min_value = unsorted_values[pos]
            pos += 1
        sorted_result.append(min_value)
        unsorted_values.remove(min_value)

    return sorted_result