from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    result_collection: List[int] = []
    i: int = 0
    while i < len(list_of_positive_integers):
        current = list_of_positive_integers[i]
        all_odd = True
        j = 0
        digits = str(current)
        while j < len(digits):
            value = int(digits[j])
            if value % 2 == 0:
                all_odd = False
                break
            j += 1
        if all_odd:
            result_collection.append(current)
        i += 1

    sorted_result: List[int] = []
    while len(result_collection) > 0:
        min_val = result_collection[0]
        min_index = 0
        k = 1
        while k < len(result_collection):
            if result_collection[k] < min_val:
                min_val = result_collection[k]
                min_index = k
            k += 1
        sorted_result.append(min_val)
        result_collection.pop(min_index)

    return sorted_result