from typing import List

def specialFilter(list_of_numbers: List[int]) -> int:
    count = 0
    odd_digits = {1, 3, 5, 7, 9}
    for number in list_of_numbers:
        if number > 10:
            number_as_string = str(number)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count