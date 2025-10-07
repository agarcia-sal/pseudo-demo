from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    number_of_odds: int = 0
    number_of_evens: int = 0

    for value in list_one:
        if value % 2 != 0:
            number_of_odds += 1

    for item in list_two:
        if not (item % 2 != 0):
            number_of_evens += 1

    if number_of_evens >= number_of_odds:
        return "YES"
    else:
        return "NO"