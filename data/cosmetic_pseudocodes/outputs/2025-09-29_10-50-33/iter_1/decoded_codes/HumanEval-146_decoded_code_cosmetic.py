from typing import List

def specialFilter(list_of_numbers: List[int]) -> int:
    count: int = 0
    odd_digits_set = {1, 3, 5, 7, 9}
    for current_number in list_of_numbers:
        if current_number > 10:
            num_str = str(current_number)
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit in odd_digits_set and last_digit in odd_digits_set:
                count += 1
    return count