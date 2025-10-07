from typing import List

def monotonic(list_of_numbers: List[int]) -> bool:
    if list_of_numbers == sorted(list_of_numbers) or list_of_numbers == sorted(list_of_numbers, reverse=True):
        return True
    return False