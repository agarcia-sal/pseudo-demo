from typing import List

def COUNT_OF_BITS_SET(num: int) -> int:
    tally = 0
    position = 0
    while position < 32:
        tally += (num >> position) & 1
        position += 1
    return tally

def sort_array(array_of_integers: List[int]) -> List[int]:
    collector = []
    for number_element in array_of_integers:
        collector.append(number_element)
    collector.sort(key=lambda x: (COUNT_OF_BITS_SET(x), x))
    return collector