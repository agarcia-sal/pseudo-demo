from typing import Iterable

def solution(collection_of_nums: Iterable[int]) -> int:
    accumulator: int = 0
    iterator: int = 0
    collection_as_list = list(collection_of_nums)  # ensure indexing if input is not indexable
    length = len(collection_as_list)
    while iterator < length:
        if (iterator % 2 == 0) and (collection_as_list[iterator] % 2 == 1):
            accumulator += collection_as_list[iterator]
        iterator += 1
    return accumulator