from typing import List


def fizz_buzz(integer_n: int) -> int:
    list_of_numbers: List[int] = []
    for integer_i in range(integer_n):
        if integer_i % 11 == 0 or integer_i % 13 == 0:
            list_of_numbers.append(integer_i)
    concatenated_string: str = ''.join(str(num) for num in list_of_numbers)
    count_of_digit_seven: int = sum(c == '7' for c in concatenated_string)
    return count_of_digit_seven