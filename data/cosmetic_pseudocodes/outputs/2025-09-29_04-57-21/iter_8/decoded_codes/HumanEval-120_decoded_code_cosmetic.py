from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    result_collection: List[int] = []
    if positive_integer_k == 0:
        return result_collection

    array_of_integers.sort()
    index_limit = len(array_of_integers) - positive_integer_k

    while index_limit < len(array_of_integers):
        result_collection.append(array_of_integers[index_limit])
        index_limit += 1

    return result_collection