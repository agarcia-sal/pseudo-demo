from typing import List


def unique_digits(sequence_of_numbers: List[int]) -> List[int]:
    container_of_odds: List[int] = []
    cursor: int = 0
    while cursor < len(sequence_of_numbers):
        number_sample: int = sequence_of_numbers[cursor]
        index_digit: int = 0
        flag_all_odd: bool = True
        digits_str: str = str(number_sample)
        # Check each digit to ensure all are odd
        while index_digit < len(digits_str) and flag_all_odd:
            digit_value: int = int(digits_str[index_digit])
            if (digit_value % 2) == 0:
                flag_all_odd = False
                break
            index_digit += 1
        if flag_all_odd:
            container_of_odds.append(number_sample)
        cursor += 1

    temp_list: List[int] = container_of_odds
    n: int = len(temp_list)
    swapped: bool = True
    # Bubble sort implementation
    while swapped:
        swapped = False
        position: int = 1
        while position < n:
            if temp_list[position - 1] > temp_list[position]:
                temp_list[position - 1], temp_list[position] = temp_list[position], temp_list[position - 1]
                swapped = True
            position += 1
        n -= 1

    return temp_list