from typing import List

def NUMBER_OF_ONES_IN_BINARY(number: int) -> int:
    binary_str = bin(number)
    trimmed_str = binary_str[2:]
    one_count = trimmed_str.count('1')
    return one_count

def sort_array(array_of_integers: List[int]) -> List[int]:
    first_sort = sorted(array_of_integers)
    result = sorted(first_sort, key=NUMBER_OF_ONES_IN_BINARY)
    return result