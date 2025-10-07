from typing import List

def double_the_difference(list_of_numbers: List[int]) -> int:
    return sum(number * number for number in list_of_numbers if number > 0 and number % 2 != 0 and "." not in str(number))