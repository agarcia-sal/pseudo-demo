from typing import List

def fizz_buzz(limit: int) -> int:
    divisible_numbers: List[int] = []
    for integer in range(limit):
        if integer % 11 == 0 or integer % 13 == 0:
            divisible_numbers.append(integer)
    concatenated_string: str = ''
    for number in divisible_numbers:
        concatenated_string += str(number)
    count_of_sevens: int = sum(char == '7' for char in concatenated_string)
    return count_of_sevens