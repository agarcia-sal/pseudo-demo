from typing import List

def fizz_buzz(integer_n: int) -> int:
    list_of_numbers: List[int] = [i for i in range(integer_n) if i % 11 == 0 or i % 13 == 0]
    concatenated_string: str = ''.join(str(number) for number in list_of_numbers)
    count_of_sevens: int = sum(c == '7' for c in concatenated_string)
    return count_of_sevens