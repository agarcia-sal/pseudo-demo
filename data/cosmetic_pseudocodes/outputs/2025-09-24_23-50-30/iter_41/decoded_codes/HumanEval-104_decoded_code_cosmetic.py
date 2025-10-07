from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def check_all_odd(number: int, position: int, digits_list: List[int]) -> bool:
        if position == len(digits_list):
            return True
        return (digits_list[position] % 2 == 1) and check_all_odd(number, position + 1, digits_list)

    intermediate_collection: List[int] = []
    index_counter = 0

    while index_counter < len(list_of_positive_integers):
        current_value = list_of_positive_integers[index_counter]
        digit_array: List[int] = []
        temp_value = current_value

        # Extract digits left-to-right
        while temp_value > 0:
            digit_array.insert(0, temp_value % 10)
            temp_value //= 10

        if check_all_odd(current_value, 0, digit_array):
            intermediate_collection.append(current_value)
        index_counter += 1

    sorted_result: List[int] = []
    for element in intermediate_collection:
        # Insert element to maintain ascending order using binary search for efficiency
        lo, hi = 0, len(sorted_result)
        while lo < hi:
            mid = (lo + hi) // 2
            if sorted_result[mid] < element:
                lo = mid + 1
            else:
                hi = mid
        sorted_result.insert(lo, element)

    return sorted_result