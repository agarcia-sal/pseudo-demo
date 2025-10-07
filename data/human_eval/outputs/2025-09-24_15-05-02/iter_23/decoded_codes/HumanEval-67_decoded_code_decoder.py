from typing import List


def fruit_distribution(string_s: str, integer_n: int) -> int:
    list_numbers: List[int] = []
    for word in string_s.split(' '):
        if word.isdigit():
            # Append integer value of word if it is a digit
            list_numbers.append(int(word))
    total_apples_and_oranges: int = sum(list_numbers)
    return integer_n - total_apples_and_oranges